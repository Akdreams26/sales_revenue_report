# 🚀 Git Commands — Step-by-Step Upload Guide
### How to Upload This Project to GitHub Professionally

---

## STEP 1 — Install Git (if not installed)
Download from: https://git-scm.com/downloads
After installing, open **Command Prompt (cmd)** or **Terminal**

---

## STEP 2 — Create Repository on GitHub
1. Go to https://github.com
2. Click **"New"** (green button)
3. Repository name: `retail-sales-analysis-python`
4. Keep it **Public**
5. Do NOT check "Add README" (we already have one)
6. Click **"Create repository"**
7. **Copy the repository URL** shown on screen
   Example: `https://github.com/your-username/retail-sales-analysis-python.git`

---

## STEP 3 — Open CMD in Your Project Folder
1. Extract the ZIP file on your computer
2. Open the `sales_project` folder
3. Click on the address bar → type `cmd` → press Enter
   *(This opens Command Prompt inside that folder)*

---

## STEP 4 — Run These Git Commands One by One

```bash
# 1. Setup your name and email (only once ever)
git config --global user.name "Aakriti Mathur"
git config --global user.email "your-email@gmail.com"

# 2. Initialize git in your project folder
git init

# 3. Connect to your GitHub repository
git remote add origin https://github.com/your-username/retail-sales-analysis-python.git

# 4. Add all files
git add .

# 5. Save with a message (first commit)
git commit -m "Initial commit: Sales & Revenue Analysis Dashboard"

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

---

## STEP 5 — Done! ✅
Go to your GitHub repository link — all files will be visible!

---

## 📝 Future Updates (When you make changes)
```bash
git add .
git commit -m "Updated analysis / added new chart"
git push
```

---

## ❓ Common Errors & Fix

| Error | Fix |
|-------|-----|
| `git not recognized` | Install Git from git-scm.com |
| `authentication failed` | Use GitHub token instead of password |
| `remote already exists` | Skip `git remote add` step |

