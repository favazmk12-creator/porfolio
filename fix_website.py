import os

# The file we want to fix
file_path = 'index.html'

# 1. READ the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. CHANGE COLORS (Yellow -> Orange)
# We replace the specific hex code used in your style
new_content = content.replace('#fdcb6e', '#F96D00')

# 3. FIX STRUCTURE (Move scripts inside body)
# The original file had </body> and </html> appearing BEFORE the scripts.
# We will remove them from the middle and add them to the very end.
if "</body>" in new_content and "<script>" in new_content:
    # Remove the premature closing tags
    new_content = new_content.replace('</body>', '').replace('</html>', '')
    
    # Add them properly at the very end of the file
    new_content = new_content.strip() + "\n</body>\n</html>"

# 4. SAVE the changes
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Success! index.html has been updated with Orange colors and fixed code structure.")
