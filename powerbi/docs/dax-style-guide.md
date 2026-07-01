# DAX Style Guide

A consistent DAX style improves readability, maintainability, and Git diff clarity.

---

## 🧱 Naming Conventions

- Measures use **PascalCase**
- Tables use **PascalCase**
- Variables use **camelCase**
- Display folders use **_Prefix Format**

Example:
- Measure: Total Revenue
- Variable: revenueToday
- Folder: _Revenue

---

## 📐 Formatting Rules

### Use indentation

### Use meaningful variable names

    
---

## 🎯 Best Practices

- Avoid SELECTEDVALUE without default
- Avoid CALCULATE inside iterators unless required
- Use DIVIDE instead of `/`
- Use COALESCE for safe defaults
- Use SWITCH(TRUE()) for multi-condition logic
- Use FORMAT only in visuals, not measures

---

## 🧪 Testing Measures

- Validate with small filtered tables
- Compare against known totals
- Check edge cases (blank, zero, negative)
