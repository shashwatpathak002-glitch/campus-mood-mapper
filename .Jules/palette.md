## 2025-05-14 - Accessible Micro-UX in Streamlit
**Learning:** Streamlit's native components have limited ARIA support. Using `st.markdown(..., unsafe_allow_html=True)` allows injecting semantic attributes like `role="region"` and `aria-label` for custom layout elements (e.g., dashboard cards).
**Action:** Use `st.markdown` for custom UI blocks that need accessibility descriptors beyond what `st.container` or `st.columns` provide.

## 2025-05-14 - Dual Purpose Tooltips
**Learning:** The `help` parameter in Streamlit form inputs (`st.text_input`, `st.slider`, etc.) acts as both a visual tooltip and provides context that helps users understand what is expected, reducing cognitive load for complex or ambiguous fields.
**Action:** Always provide `help` text for fields that aren't self-explanatory or have specific constraints.

## 2025-05-14 - Playwright & Streamlit Radio Buttons
**Learning:** Streamlit hides the actual `<input type="radio">` element. Playwright's `check()` method fails because the element is not visible.
**Action:** Use `page.get_by_text('Label', exact=True).click()` to interact with Streamlit radio buttons in automated tests.
