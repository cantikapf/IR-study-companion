import pytest
from pathlib import Path
from scripts.sync_youtube_video import (
    extract_youtube_id,
    find_chapter_file,
    update_chapter_frontmatter,
)

def test_extract_youtube_id():
    # Full watch url
    assert extract_youtube_id("https://www.youtube.com/watch?v=F31-IkqM-Qg") == "F31-IkqM-Qg"
    # Short youtu.be url
    assert extract_youtube_id("https://youtu.be/F31-IkqM-Qg") == "F31-IkqM-Qg"
    # Embed url
    assert extract_youtube_id("https://www.youtube.com/embed/F31-IkqM-Qg") == "F31-IkqM-Qg"
    # Bare ID
    assert extract_youtube_id("F31-IkqM-Qg") == "F31-IkqM-Qg"
    # With query parameters
    assert extract_youtube_id("https://youtu.be/F31-IkqM-Qg?si=abcdef123") == "F31-IkqM-Qg"
    assert extract_youtube_id("https://www.youtube.com/watch?v=F31-IkqM-Qg&feature=shared") == "F31-IkqM-Qg"

def test_extract_youtube_id_invalid():
    with pytest.raises(ValueError):
        extract_youtube_id("not_a_valid_youtube_url")

def test_find_chapter_file():
    # Match by number
    f = find_chapter_file("010")
    assert f.exists()
    assert "010-ir-study" in f.name

    # Match by CH prefix
    f = find_chapter_file("CH030")
    assert f.exists()
    assert "030-basic-realism" in f.name

    # Match by slug
    f = find_chapter_file("basic-marxism")
    assert f.exists()
    assert "050-basic-marxism" in f.name

def test_update_chapter_frontmatter(tmp_path: Path):
    sample_file = tmp_path / "080-global-environment.md"
    sample_file.write_text(
        "---\n"
        "title: Global Environment As Agendas\n"
        "slug: global-environment-as-agendas\n"
        "abstract: Environmental politics\n"
        "---\n\n"
        "## Introduction\n"
        "Sample body content.\n",
        encoding="utf-8"
    )

    title, slug = update_chapter_frontmatter(sample_file, "TEST_YT_123")
    assert title == "Global Environment As Agendas"
    assert slug == "global-environment-as-agendas"

    content = sample_file.read_text(encoding="utf-8")
    assert 'youtube_id: "TEST_YT_123"' in content
    assert 'status: "Published"' in content
    assert "## Introduction" in content
