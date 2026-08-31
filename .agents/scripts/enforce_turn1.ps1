param()
try {
    # Read STDIN
    $inputData = $input | Out-String | ConvertFrom-Json
    
    # Check if it's the first invocation of the session
    if ($inputData.invocationNum -eq 1) {
        $response = @{
            injectSteps = @(
                @{
                    ephemeralMessage = "[SYSTEM OVERRIDE: TURN 1 ENFORCEMENT] You are entering Turn 1 of a new session. You MUST immediately recall and apply all guidelines from 'lessons-learned.md' and 'second-brain-rule.md'. Do not skip this."
                }
            )
        }
        $response | ConvertTo-Json -Depth 10 -Compress | Write-Host
    } else {
        Write-Host "{}"
    }
} catch {
    Write-Host "{}"
}
