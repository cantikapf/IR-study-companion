const { test, expect } = require('@playwright/test');

test.describe('IR Study Companion UI Interactive Features', () => {
  
  test.beforeEach(async ({ page }) => {
    // Navigate to a known chapter that has quiz and flashcards
    await page.goto('/poverty-development-aid.html');
  });

  test('Quiz Option Click and Feedback', async ({ page }) => {
    const submitBtn = page.locator('.quiz-submit').first();
    
    // Extract correct index from onclick="submitQuiz('id', 'correctIdx')"
    const onclickStr = await submitBtn.getAttribute('onclick');
    const match = onclickStr.match(/',\s*'(\d+)'\)/);
    const correctIdx = match ? match[1] : '1';

    // Find and click the correct option
    const correctOption = page.locator(`.quiz-option[data-idx="${correctIdx}"]`).first();
    await expect(correctOption).toBeVisible();
    await correctOption.click();

    // Click submit
    await submitBtn.click();

    // The feedback section should become visible
    const feedback = page.locator('.quiz-feedback').first();
    await expect(feedback).toBeVisible();
    await expect(feedback).not.toBeEmpty();

    // Check if localStorage has been updated for this quiz
    const containerId = await page.locator('.quiz-container').first().getAttribute('id');
    const baseId = containerId.replace('quiz-', '');
    const storedState = await page.evaluate((id) => localStorage.getItem('quiz_' + id + '_completed'), baseId);
    expect(storedState).toBeTruthy();
  });

  test('Flashcard Flip Interaction', async ({ page }) => {
    const flashcard = page.locator('.flashcard').first();
    await expect(flashcard).toBeVisible();
    
    // Check initial state (aria-expanded should be false)
    await expect(flashcard).toHaveAttribute('aria-expanded', 'false');

    // Click the flashcard
    await flashcard.click();

    // Wait a brief moment
    await page.waitForTimeout(300);

    // After click, it should have class flipped
    await expect(flashcard).toHaveClass(/flipped/);
    await expect(flashcard).toHaveAttribute('aria-expanded', 'true');
  });

  test('Dark Mode Toggle', async ({ page }) => {
    const themeToggle = page.locator('#dark-mode-btn');
    await expect(themeToggle).toBeVisible();

    // Click to toggle
    await themeToggle.click();

    // Verify localStorage has a theme saved
    const savedTheme = await page.evaluate(() => localStorage.getItem('theme'));
    expect(['dark', 'light']).toContain(savedTheme);

    // Verify body class is synced
    if (savedTheme === 'dark') {
      await expect(page.locator('body')).toHaveClass(/dark-theme/);
    } else {
      await expect(page.locator('body')).not.toHaveClass(/dark-theme/);
    }
  });

});
