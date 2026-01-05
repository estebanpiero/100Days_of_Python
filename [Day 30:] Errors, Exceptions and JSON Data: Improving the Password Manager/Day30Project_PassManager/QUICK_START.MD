# 🚀 Quick Start Guide

## Installation

1. Make sure you have Python 3.7+ installed
2. Save the `password_manager_advanced.py` file
3. (Optional) Add a `logo.png` image in the same directory
4. Run the program:
   ```bash
   python password_manager_advanced.py
   ```

## First Time Setup

1. The program will create a `data.json` file automatically when you save your first password
2. Change the `DEFAULT_EMAIL` constant in the code to your email for convenience

## Interface Layout

```
┌─────────────────────────────────────────────┐
│              🔐 (Logo)                      │
│      Advanced Password Manager              │
├─────────────────────────────────────────────┤
│ Website:      [____________] [🔍 Search]    │
│ Email:        [_________________________]   │
│ Password:     [____________] [🎲][👁]       │
│               Strength: Strong              │
├─────────────────────────────────────────────┤
│         [💾 Save Password]                  │
├─────────────────────────────────────────────┤
│  [📋 Copy] [🗑️ Delete] [👁️ View All]       │
│  [📊 Statistics] [💾 Export Data]           │
├─────────────────────────────────────────────┤
│   Built with Python & Tkinter 🔒            │
└─────────────────────────────────────────────┘
```

## Common Workflows

### Workflow 1: Creating a New Password

1. Click in "Website" field (auto-focused on startup)
2. Type website name (e.g., "github.com")
3. Email field already has default email (change if needed)
4. Click "🎲 Generate" to create strong password
5. Check the strength indicator (aim for "Strong")
6. Click "💾 Save Password"
7. Confirmation dialog appears
8. Click OK to save

**Time**: ~10 seconds

### Workflow 2: Retrieving a Password

1. Type website name in "Website" field
2. Click "🔍 Search"
3. Info dialog shows credentials
4. Password automatically fills in field
5. Click "📋 Copy" to copy to clipboard
6. Paste wherever needed

**Time**: ~5 seconds

### Workflow 3: Updating an Existing Password

1. Type website name
2. Click "🔍 Search" (loads current password)
3. Click "🎲 Generate" for new password
4. Click "💾 Save Password"
5. Confirm overwrite when asked

**Time**: ~8 seconds

### Workflow 4: Security Audit

1. Click "📊 Statistics"
2. Review password strength breakdown
3. Note any weak passwords
4. Click "👁️ View All" to see all entries
5. Update weak passwords one by one

**Time**: ~2 minutes for 10-20 passwords

### Workflow 5: Backing Up Data

1. Click "💾 Export Data"
2. File saved as `password_export_YYYYMMDD_HHMMSS.txt`
3. Move file to secure location (USB drive, encrypted folder)
4. Store `data.json` backup separately

**Time**: ~30 seconds

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Focus Website field | Tab or click |
| Focus Email field | Tab |
| Focus Password field | Tab |
| Save (when dialog open) | Enter |
| Cancel (when dialog open) | Esc |

## Tips & Tricks

### 💡 Pro Tips

1. **Use the Statistics Feature Regularly**
   - Check monthly for weak passwords
   - Aim for 100% "Strong" passwords

2. **Naming Convention**
   - Use consistent naming: "github.com" not "GitHub" or "github"
   - Makes searching easier

3. **Email Management**
   - Change default email in code if you use different emails
   - Or manually edit for each site

4. **Regular Backups**
   - Export data monthly
   - Keep `data.json` in version control (encrypted repo)

5. **Password Strength**
   - Always aim for "Strong" rating
   - Minimum 12 characters recommended
   - Use generated passwords when possible

### ⚠️ Common Mistakes

1. **Don't forget to save after generating**
   - Generated password only saved when you click "💾 Save"

2. **Check before deleting**
   - Deletion is permanent!
   - Export data first if uncertain

3. **Keep exports secure**
   - Exported files are plain text
   - Encrypt or store in secure location

4. **Watch for duplicates**
   - Program warns about overwriting
   - Read confirmation dialogs carefully

## Troubleshooting

### Problem: Logo doesn't appear
**Solution**: Place `logo.png` in same folder, or ignore - program uses emoji instead

### Problem: Can't find saved passwords
**Solution**: Check `data.json` file exists in same folder as program

### Problem: Program crashes on startup
**Solution**: Delete corrupted `data.json` and restart (backup first!)

### Problem: Copy to clipboard doesn't work
**Solution**: Some Linux systems need `xclip` installed:
```bash
sudo apt-get install xclip
```

### Problem: Entries not aligned
**Solution**: This version has proper alignment - make sure you're using `password_manager_advanced.py`

## Security Best Practices

### ✅ Do This

- ✅ Generate passwords with the tool
- ✅ Use unique passwords for each site
- ✅ Regularly check statistics
- ✅ Update weak passwords
- ✅ Keep backups encrypted
- ✅ Use strong master password (if implementing encryption)

### ❌ Don't Do This

- ❌ Don't reuse passwords
- ❌ Don't share `data.json` file
- ❌ Don't use weak passwords
- ❌ Don't leave exports in plain sight
- ❌ Don't skip backups
- ❌ Don't save passwords in shared locations

## Advanced Usage

### For Power Users

1. **Batch Import** (modify code):
   - Add CSV import function
   - Parse from other password managers

2. **Encryption** (future):
   - Add master password
   - Encrypt `data.json` with cryptography library

3. **Categories** (modify code):
   - Add "category" field to data structure
   - Filter by category in "View All"

4. **Browser Integration**:
   - Create simple REST API
   - Build browser extension

## Data Management

### Manual JSON Editing

You can manually edit `data.json` if needed:

```json
{
  "example.com": {
    "email": "user@email.com",
    "password": "SecurePass123!",
    "created": "2026-01-05 10:00:00",
    "modified": "2026-01-05 10:00:00"
  }
}
```

### Backup Strategy

**Daily**: Automatic with program running
**Weekly**: Export to external drive
**Monthly**: Cloud backup (encrypted)
**Yearly**: Print critical passwords (secure location)

## Getting Help

If you need help:
1. Check this guide first
2. Review the README.md
3. Check the code comments
4. Test with dummy data first

## Next Steps

Once comfortable with basic features:
1. ⭐ Add encryption for security
2. ⭐ Implement master password
3. ⭐ Add password expiry warnings
4. ⭐ Create backup automation
5. ⭐ Build browser extension

---

**Happy Password Managing! 🔐**
