# Energy Gym Assistant: AI Customer Service Agent for Energy Gym

Energy Gym Assistant is an intelligent customer service agent built for Energy Gym. It helps prospective and current members quickly query business hours, search course availability, calculate membership fees with multi-month discounts, and request human staff support.

> Course homework: Unit G, My AI Customer Service Agent, with a Database and Tools  
> Student: F115118132 劉保鑫

## Who It Serves and When They Use It

- **Who uses it:** Prospective members looking for gym details or fee plans, and existing members checking class schedules.
- **When they use it:** Anytime, especially during off-hours when phone support is unavailable.
- **What problem it solves:** Eliminates phone hold times and static FAQ searches by providing instant, deterministic responses and automated discount calculations.

## What It Can Do

| Function | Example question | Tool it uses |
|---|---|---|
| Query opening hours and gym info | "請問你們幾點開門？" | `get_gym_info` |
| Check course availability and schedules | "週一晚上的瑜珈班還有名額嗎？" | `check_class` |
| Calculate multi-month membership fees | "我要買單月會籍，連續買 4 個月總共要多少錢？" | `calculate_fee` |
| Transfer to human customer support | "你們的教練態度很差，我要找主管！" | `transfer_to_human` |

## How It Works

Every question goes to the agent first. The agent chooses a tool, the tool reads the database or calculates in code, and the agent answers strictly based on what the tool returns.

- **Model:** Gemini
- **Chat screen:** Gradio Web UI
- **Database (SQLite):** `gym_app.db`, built dynamically from CSV files at startup.

  | Table | CSV file | What it holds | Rows |
  |---|---|---|---|
  | `gym_info` | `gym_info.csv` | Gym opening hours, location, rules, and general FAQs | 9 topics |
  | `classes` | `classes.csv` | Course names, days, prices, and remaining spots | 15 rows |

- **Tools:**

  | Tool | What it does |
  |---|---|
  | `get_gym_info(topic)` | Reads matching topic content from the `gym_info` table |
  | `check_class(class_name)` | Finds class schedules and available spots from the `classes` table |
  | `calculate_fee(price, months)` | Computes total fee (`price * months`), applying a 10% discount for 3+ months |
  | `transfer_to_human()` | Provides phone number and official LINE ID for human support |

## Sample Conversations

- **Tool Execution & Calculation:** Automatically queries single-month pricing and applies discount rules when calculating multi-month membership fees.
- **Out of Scope Handling:** Politely declines non-gym queries (e.g., asking for nearby restaurants) without invoking tools.

## Project Files

```text
Homework-Report/
├── app-gradio.py       # Main agent application: database setup, tools, and Gradio chat interface
├── test_tool.py        # Automated testing script for tool-choice routing evaluation
├── gym_info.csv        # Information table (FAQ & store details)
├── classes.csv         # Records table (Class schedules & spots)
├── .gitignore          # Excludes sensitive files (.env and *.db) from repository
└── README.md           # Project documentation
```

## How to Install and Run It

1. Clone the project repository:

   ```bash
   git clone https://github.com/Blake-0716/Homework-Report.git
   cd Homework-Report
   ```

2. Install required dependencies (Python 3.10+):

   ```bash
   pip install gradio google-generativeai python-dotenv
   ```

3. Set up environment configuration:
   Create a `.env` file in the root directory and insert your Gemini API Key:

   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. Launch the agent:

   ```bash
   python app-gradio.py
   ```

5. Open the local URL displayed in the console (usually `[http://127.0.0.1:7860](http://127.0.0.1:7860)`).

6. Run the automated tool-choice test:

   ```bash
   python test_tool.py
   ```

## Notes

- All member contact details, prices, and schedules are created for demonstration purposes.
- The `.env` file containing the API key and local `.db` files are strictly excluded via `.gitignore` to protect security.
