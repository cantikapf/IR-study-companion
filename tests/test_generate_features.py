import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import patch, MagicMock, mock_open

# Set environment variable before import
os.environ["GROQ_API_KEY"] = "fake_key"

# Create a mock openai module
mock_openai = MagicMock()
mock_client_instance = MagicMock()
mock_openai.OpenAI.return_value = mock_client_instance

# Setup fake models list so the script doesn't crash on import
mock_model = MagicMock()
mock_model.id = "llama-3-8b"
mock_client_instance.models.list.return_value.data = [mock_model]

sys.modules['openai'] = mock_openai

import generate_features

def test_process_file_success(mocker):
    mock_client_instance.chat.completions.create.reset_mock()
    mocked_content = "Some text.\nWhich of the following best summarizes the core concept discussed in this chapter?\n### Interactive Learning old stuff"
    m_open = mocker.patch("builtins.open", mock_open(read_data=mocked_content))
    
    fake_response = MagicMock()
    fake_response.choices[0].message.content = '''
    {
      "flashcards": [
        {"term": "T1", "def": "D1"},
        {"term": "T2", "def": "D2"},
        {"term": "T3", "def": "D3"},
        {"term": "T4", "def": "D4"}
      ],
      "quiz": {
        "question": "Q?",
        "opt1": "O1",
        "opt2": "O2",
        "opt3": "O3",
        "opt4": "O4",
        "correct": "1"
      }
    }
    '''
    mock_client_instance.chat.completions.create.return_value = fake_response
    
    generate_features.process_file("dummy.md")
    
    # Check if file was written to
    m_open.assert_called_with("dummy.md", "w", encoding="utf-8")
    
    # Get what was written
    handle = m_open()
    written_args = handle.write.call_args[0][0]
    
    assert "### Interactive Learning" in written_args
    assert "term1=\"T1\" def1=\"D1\"" in written_args
    assert "id=\"quiz_dummy\"" in written_args

def test_process_file_skip_no_generic_quiz(mocker):
    mock_client_instance.chat.completions.create.reset_mock()
    mocked_content = "Already has contextual quiz."
    mocker.patch("builtins.open", mock_open(read_data=mocked_content))
    
    generate_features.process_file("dummy.md")
    
    mock_client_instance.chat.completions.create.assert_not_called()

def test_process_file_api_rate_limit(mocker):
    mock_client_instance.chat.completions.create.reset_mock()
    mocked_content = "Which of the following best summarizes the core concept discussed in this chapter?"
    mocker.patch("builtins.open", mock_open(read_data=mocked_content))
    
    mock_sleep = mocker.patch("time.sleep")
    
    fake_response = MagicMock()
    fake_response.choices[0].message.content = '{"flashcards": [{"term": "T1", "def": "D1"},{"term": "T1", "def": "D1"},{"term": "T1", "def": "D1"},{"term": "T1", "def": "D1"}], "quiz": {"question": "Q?", "opt1": "1", "opt2": "2", "opt3": "3", "opt4": "4", "correct": "1"}}'
    
    mock_client_instance.chat.completions.create.side_effect = [
        Exception("429 rate limit exceeded"),
        Exception("Rate limit reached"),
        fake_response
    ]
    
    generate_features.process_file("dummy.md")
    
    assert mock_sleep.call_count == 2
