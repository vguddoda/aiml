🔐 GITHUB TOKEN FIX GUIDE

================================================================================
❌ PROBLEM
================================================================================

Error: "The `models` permission is required to access this endpoint"

This means your token doesn't have permission to use GitHub Models API.

================================================================================
✅ SOLUTION (3 Options)
================================================================================

OPTION 1: USE CLASSIC TOKEN (Easiest & Most Reliable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Go to: https://github.com/settings/tokens
   (Note: NO ?type=beta at the end)

2. Click "Generate new token" at the top right

3. In the form:
   - Token name: "AI Agent Models"
   - Expiration: 30 days (or your preference)
   
4. Select these SCOPES:
   ✅ repo (full control of private repositories)
   ✅ read:packages (read packages)
   ✅ gist (create gists)
   
5. Click "Generate token" button (green button at bottom)

6. COPY THE TOKEN (starts with ghp_)

7. Add to your .env file (see instructions below)


OPTION 2: FINE-GRAINED TOKEN (More Control)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Go to: https://github.com/settings/tokens?type=beta

2. Click "Generate new token"

3. In "Repository access" section:
   ✅ Select "All repositories" or "Public repositories (read-only)"

4. In "Permissions" section - Click "Add permissions" dropdown

5. In the dropdown, SCROLL DOWN and find:
   ✅ Account → user:email
   ✅ Account → read:user
   ✅ Repository → contents (read)
   
6. Click "Generate token"

7. COPY THE TOKEN

8. Add to your .env file (see instructions below)


OPTION 3: QUICK FIX (Use Personal Access Token)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Go to: https://github.com/settings/personal-access-tokens/new

2. Name: "AI Models"

3. Expiration: 30 days

4. Select all "Account" permissions (check the main boxes)

5. Generate and copy token

================================================================================
📝 UPDATE YOUR .ENV FILE
================================================================================

After getting your new token:

1. Open the file: .env
   Command: nano /Users/vishalkumarbg/Documents/AI_ML_DOCS/aiml/.env

2. Replace the old token with your new one:
   FROM:
   GITHUB_TOKEN=old_token_here
   
   TO:
   GITHUB_TOKEN=ghp_your_new_token_here

3. Save the file:
   Press: Ctrl+O (Enter) then Ctrl+X

4. Test it:
   python3 simple_agent.py

================================================================================
🧪 TEST IF IT WORKS
================================================================================

After updating .env, run:

   python3 test_agent.py

You should see:
   ✅ PASS: LLM connection successful

If you see that, your agent will work!

================================================================================
🚀 IF YOU'RE STILL STUCK
================================================================================

Try this simpler agent (no token issues):

   python3 simple_agent.py

This version only uses:
   - Calculator (no API needed)
   - Time (no API needed)

No GitHub token required for basic math!

================================================================================
💡 QUICK REMINDER
================================================================================

Your token = Password to GitHub Models API
- Keep it SECRET ⚠️
- Don't share it ⚠️
- Don't commit it to git ⚠️
- Add .env to .gitignore ⚠️

Create a NEW token if you think it's been exposed!

================================================================================
Need help? Check:
- QUICKSTART.md (setup guide)
- CONCEPTS.md (how agents work)
- INSTALLATION_SUCCESS.txt (what's installed)

Happy building! 🚀
