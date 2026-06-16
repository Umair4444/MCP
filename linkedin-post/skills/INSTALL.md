# Skill Installation Guide

This folder contains specialized Gemini CLI skills for LinkedIn content strategy and visual design. Follow these steps to install and activate them.

## 1. Installation

You can install these skills either for this specific workspace or globally for all projects.

### Workspace Scope (Recommended for this project)
Run these commands from the project root:

```powershell
gemini skills install skills/linkedin-post.skill --scope workspace
gemini skills install skills/canva-linkedin-design.skill --scope workspace
gemini skills install skills/topic-archiver.skill --scope workspace
```

### User Scope (Global)
Run these commands if you want the skills available in every project:

```powershell
gemini skills install skills/linkedin-post.skill --scope user
gemini skills install skills/canva-linkedin-design.skill --scope user
gemini skills install skills/topic-archiver.skill --scope user
```

## 2. Activation

After installation, you **must** reload your skills in your active Gemini CLI session to enable them:

```bash
/skills reload
```

## 3. Verification

To verify that the skills are correctly installed and loaded, run:

```bash
/skills list
```

You should see `linkedin-post`, `canva-linkedin-design`, and `topic-archiver` in the list.

## 4. Usage

Once active, you can simply ask the agent to help with LinkedIn tasks:
- "Create a LinkedIn post about [Topic]"
- "Plan a Canva carousel for [Topic]"
- "Optimize this draft using the LinkedIn skill"
