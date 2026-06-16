---
name: topic-archiver
description: Archive LinkedIn posts into a topic folder with clean plain text, multi-slide carousel images, and a scrollable HTML preview. Supports single images, PDF carousels (via slide thumbnails), and direct PDF downloads.
---

# Topic Archiver

This skill provides a standardized workflow for creating a complete archive of LinkedIn posts, including complex multi-page carousels.

## Workflow

1. **Normalize the Topic**:
   - Folder: `archives/<normalized-topic>/`.

2. **Save Clean Text (`post.txt`)**:
   - Convert the post content into a clean plain text format.
   - **CLEANING RULES**: 
     - Remove Markdown formatting characters (e.g., remove `**` for bold, `#` for headers, `_` for italics).
     - **KEEP EMOJIS**: Do not remove emojis; they preserve the post's tone.
     - Keep original line breaks and spacing.
   - Use `write_file` to save the cleaned text to `archives/<normalized-topic>/post.txt`.

3. **Handle Visual Assets (Images/Carousels/PDFs)**:
   - **Case A: Single Image**:
     - Download as `image.png` using PowerShell `Invoke-WebRequest`.
   - **Case B: Multi-page Carousel**:
     - Download each slide thumbnail provided by Canva as `slide-1.png`, `slide-2.png`, etc.
   - **Case C: PDF Document**:
     - Download the final PDF as `document.pdf` if a download link is provided.

4. **Generate HTML Preview (`preview.html`)**:
   - Use `write_file` to create a preview using the following LinkedIn-simulated structure:
     - **Styles**: Use `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto` font, `#f3f2ef` body background, and a white, bordered container with a light box-shadow.
     - **Structure**:
       - Header: Include a placeholder avatar, author name, and headline.
       - Post Text: Plain text with `white-space: pre-line`.
       - Carousel: Interactive, JS-driven, toggling `active` class on `slide-N.jpg` images with Previous/Next buttons.
       - Interaction Bar: Include SVG icons for "Like", "Comment", "Repost", and "Send".
   - Ensure the template is consistent with the latest LinkedIn UI standards.

5. **Verify and Confirm**:
   - Ensure all assets are saved and the HTML preview links to them correctly.

## Example
If archiving "Agent Factory":
- Clean text: "The future of Enterprise AI isn't the single bot—it’s the Agent Factory." (no bold stars)
- Save to: `archives/agent-factory/post.txt`
