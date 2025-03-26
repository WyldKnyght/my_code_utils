The error occurs because the `imp` module (used in `importanize`) was deprecated in Python 3.4 and **removed in Python 3.12**. This indicates you're using a Python version ≥3.12, while `importanize` appears unmaintained (last GitHub commit was in 2019).

## Solutions

### 1. Quick Fix: Use Python ≤3.11
```bash
# Example using pyenv (recommended):
pyenv install 3.11.9
pyenv local 3.11.9
python -m pip install importanize
```

### 2. Patch importanize (For Python ≥3.12)
1. **Edit the problematic file**:
   Locate `site-packages/importanize/utils.py` and change:
   ```python
   import imp  # ← Remove this line
   import importlib.util  # ← Add this line
   ```
   
2. **Replace this code**:
   ```python
   # Original line 14-15:
   _, _, is_std = imp.find_module(module_part)
   ```
   With:
   ```python
   spec = importlib.util.find_spec(module_part)
   is_std = spec.origin is not None and "lib/python" in spec.origin
   ```

### 3. Recommended Alternatives
These actively maintained tools offer similar import sorting:
```bash
# isort (most popular)
pip install isort
isort your_file.py

# reorder-python-imports (Black-compatible)
pip install reorder-python-imports
reorder-python-imports your_file.py
```

## Why This Happened
- The `imp` module was fully removed in Python 3.12 ([PEP 594](https://peps.python.org/pep-0594/#imp))
- `importanize` hasn't been updated since 2019 and doesn't support modern Python versions
- GitHub repo shows no recent activity, suggesting it's abandoned

For long-term use, we recommend switching to `isort` which has better maintenance and Python 3.12+ support.

Citations:
[1] https://github.com/miki725/importanize/tree/master

---
Answer from Perplexity: pplx.ai/share