# Energy Gym Assistant: AI Customer Service Agent for Energy Gym

Energy Gym Assistant is an intelligent customer service agent built for Energy Gym. It helps prospective and current members quickly query business hours, search course availability, calculate membership fees with multi-month discounts, understand complex contract policies (leaves of absence, refunds, and transfers) through RAG, and request human staff support.

> Course homework: Midterm Project - AI Customer Service Agent with Tool Calling and RAG
> Student: F115118132 劉保鑫

## Who It Serves and When They Use It

- **Who uses it:** Prospective members looking for gym details or fee plans, and existing members checking class schedules or contract policies.
- **When they use it:** Anytime, especially during off-hours when phone support is unavailable.
- **What problem it solves:** Eliminates phone hold times and static FAQ searches by providing instant, deterministic responses, automated discount calculations, and accurate policy lookups without AI hallucination.

## What It Can Do

| Function | Example question | Tool it uses |
|---|---|---|
| Query opening hours and gym info | "請問你們幾點開門？" | `get_gym_info` |
| Check course availability and schedules | "週一晚上的瑜珈班還有名額嗎？" | `check_class` |
| Calculate multi-month membership fees | "我要買單月會籍，連續買 4 個月總共要多少錢？" | `calculate_fee` |
| **Search contract, refund & leave policies** | **"我摔斷腿了可以暫停會籍嗎？需要付錢嗎？"** | **`search_policy`** |
| Transfer to human customer support | "你們的教練態度很差，我要找主管！" | `transfer_to_human` |

## How It Works

Every question goes to the agent first. The agent chooses a tool, the tool reads the database, calculates in code, or searches the RAG document, and the agent answers strictly based on what the tool returns.

- **Model:** Gemini 1.5 Flash (integrated via OpenAI Python SDK wrapper)
- **Chat screen:** Gradio Web UI
- **Knowledge Base:**
  - **SQLite Database:** `gym_app.db`, built dynamically from CSV files at startup for structured data (`gym_info.csv`, `classes.csv`).
  - **RAG Document:** `gym_policy.md`, a markdown file containing detailed rules, penalties, and conditions, queried via keyword chunking.

- **Tools:**

  | Tool | What it does |
  |---|---|
  | `get_gym_info(topic)` | Reads matching topic content from the `gym_info` table |
  | `check_class(class_name)` | Finds class schedules and available spots from the `classes` table |
  | `calculate_fee(price, months)` | Computes total fee (`price * months`), applying a 10% discount for 3+ months |
  | **`search_policy(query)`** | **Retrieves specific contract rules from `gym_policy.md` using keyword chunk matching (RAG)** |
  | `transfer_to_human()` | Provides phone number and official LINE ID for human support |

## Sample Conversations

- **RAG Policy Retrieval:** Accurately extracts conditions and fees (e.g., "NT$500 transfer fee" or "medical proof required for free suspension") directly from the policy document.
- **Out of Scope & Defense Handling:** Politely declines non-gym queries (e.g., asking for nearby restaurants) and strictly refuses to fabricate fake data or bypass pricing rules when prompted.

## Project Files

```text
Midterm-Project/
├── app-gradio.py       # Main agent application: database setup, tools, RAG, and Gradio chat interface
├── test_tool.py        # Automated testing script for tool-choice routing evaluation
├── gym_policy.md       # Knowledge base for RAG (Membership contracts, refunds, leave policies)
├── gym_info.csv        # Information table (FAQ & store details)
├── classes.csv         # Records table (Class schedules & spots)
├── requirements.txt    # Required Python packages (gradio, openai, python-dotenv)
├── .env.example        # Environment variable template
├── .gitignore          # Excludes sensitive files (.env and *.db) from repository
└── README.md           # Project documentation
```

## How to Install and Run It

1. Clone the project repository:

   ```bash
   git clone [https://github.com/Blake-0716/Midterm-Project.git](https://github.com/Blake-0716/Midterm-Project.git)
   cd Midterm-Project
   ```

2. Install required dependencies (Python 3.10+):

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment configuration:
   Copy `.env.example` to create a `.env` file in the root directory and insert your API configuration:

   ```env
   MODEL_NAME=gemini-1.5-flash
   API_KEY=your_actual_api_key_here
   LLM_API_URL=[https://generativelanguage.googleapis.com/v1beta/openai/](https://generativelanguage.googleapis.com/v1beta/openai/)
   ```

4. Launch the agent:

   ```bash
   python app-gradio.py
   ```

5. Open the local URL displayed in the console (usually `http://127.0.0.1:7860`).

## Notes

- All member contact details, prices, and schedules are created for demonstration purposes.
- The `.env` file containing the API key and local `.db` files are strictly excluded via `.gitignore` to protect security.
