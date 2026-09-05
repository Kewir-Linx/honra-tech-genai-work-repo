## Streamlit Hands-On Tasks (`03-09-streamlit`)

Welcome to your Streamlit practical assignment! In this task, you will revise core Streamlit concepts you learned in `hello_world.py` (titles, sidebars, text inputs, sliders, session state) while introducing new UI components such as **forms**, **tabs**, **radio buttons**, **containers**, **expanders**, and **markdown formatting**.

---

#### Git Setup & Workflow

1. **Fork** this repository to your personal GitHub account.
2. **Clone** your fork to your local machine.
3. **Create and switch to a feature branch** for your work:
   ```bash
   git checkout -b feature/streamlit-task
   ```

---

#### Environment Setup

1. Initialize a uv project, then create and activate a uv virtual environment.
2. Install `streamlit`.

---

#### Student Workspace Setup

Before starting on the tasks, set up your dedicated workspace folder inside `03-09-streamlit`:

1. Create a folder named after yourself inside `03-09-streamlit/` (e.g., `03-09-streamlit/john_doe/`).
2. Copy the starter files from `task1/app.py` and `task2/app.py` into your new folder:
   * Copy `task1/app.py` -> `03-09-streamlit/john_doe/task1_app.py`
   * Copy `task2/app.py` -> `03-09-streamlit/john_doe/task2_app.py`

---

#### Using the Hints Folder

Inside `hints/`, you will find standalone, minimal Streamlit scripts for new components that you did not encounter in your previous class. You can run these individually to see how each component looks and behaves on the UI:

- `streamlit run 03-09-streamlit/hints/markdown.py`
- `streamlit run 03-09-streamlit/hints/forms.py`
- `streamlit run 03-09-streamlit/hints/radio.py`
- `streamlit run 03-09-streamlit/hints/tabs.py`
- `streamlit run 03-09-streamlit/hints/containers_and_expanders.py`
- `streamlit run 03-09-streamlit/hints/pages.py`
- `streamlit run 03-09-streamlit/hints/misc.py`

---

#### Assignment Tasks

In both tasks, you will be provided with an incomplete Python script that contains **about 2 intentional errors** (bugs/syntax issues) and missing logic marked with `# TODO:` comments. Your job is to:
1. Watch the reference screen recording video provided by your instructor to see what the final output should look like.
2. Debug and fix the errors in the code.
3. Complete the `# TODO:` sections so your app matches the target video.

##### Task 1: GenAI Prompt Generator (`task1_app.py`)
- Revise: Page config, titles, sidebar sliders, text inputs, session state.
- New components: `st.form`, `st.form_submit_button`, `st.tabs`, `st.progress`, `st.markdown`.
- Goal: Fix the code bugs and build a form that captures user details and prompt instructions, simulates generation with a progress bar, and displays the prompt and output in clean tabs.

##### Task 2: AI Model Hub & Playground (`task2_app.py`)
- Revise: Sidebar controls, text areas, layout structure.
- New components: `st.sidebar.radio` (multi-page navigation), `st.container(border=True)`, `st.expander`.
- Goal: Fix the navigation bugs and build a multi-page hub with a "Home" dashboard, a "Model Playground" with bordered result containers, and an "About & Docs" section.

---

#### Submission

Once both tasks are complete and working:
1. Add and commit your changes:
   ```bash
   git add 03-09-streamlit/your_name/
   git commit -m "Complete Streamlit tasks 1 and 2"
   ```
2. Push your feature branch to your GitHub fork:
   ```bash
   git push origin feature/streamlit-task
   ```
3. Go to GitHub and open a **Pull Request** against the original repository.
