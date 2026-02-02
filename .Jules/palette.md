## 2025-05-22 - Improving Form Guidance in Streamlit
**Learning:** In Streamlit, the `help` parameter is a powerful yet underutilized tool for providing micro-copy guidance and improving accessibility. Pair it with clear `st.caption` for required field explanations to reduce cognitive load.
**Action:** Always check if complex or critical form inputs can benefit from a `help` tooltip or a descriptive `placeholder`.

## 2025-05-22 - Deprecation of `use_column_width`
**Learning:** Streamlit has replaced `use_column_width` with `use_container_width` across many components (images, charts, etc.). Using the newer parameter avoids console warnings and ensures future compatibility.
**Action:** Use `use_container_width=True` instead of `use_column_width=True` for all layout-responsive components in Streamlit apps.
