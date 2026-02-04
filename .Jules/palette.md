## 2025-05-14 - Streamlit Help Tooltips and Playwright Selectors
**Learning:** Streamlit's `help` parameter on input widgets (like `st.text_input`) creates an additional interactive button with the same label (ARIA-labeled as "Help for [Label]"). This causes `page.get_by_label("Label")` to fail in Playwright due to strict mode violations (multiple matches).
**Action:** Use more specific locators like `page.get_by_role("textbox", name="Label")` to target the input field specifically, or `page.get_by_label("Help for [Label]")` if targeting the tooltip.

## 2025-05-14 - Character Counters in Streamlit
**Learning:** Setting the `max_chars` parameter in `st.text_area` or `st.text_input` automatically enables a native Streamlit character counter in the UI.
**Action:** Always prefer using `max_chars` for limited text inputs to provide instant feedback to the user without custom JS or complex state management.
