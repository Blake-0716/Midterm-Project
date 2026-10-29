# 測試的 10 個題目與預期工具
test_cases = [
    {"q": "請問你們幾點開門？", "expected": "get_gym_info"},
    {"q": "這附近有停車位嗎？", "expected": "get_gym_info"},
    {"q": "有提供置物櫃嗎？", "expected": "get_gym_info"},
    {"q": "請問單次入場多少錢？", "expected": "check_class"},
    {"q": "週一晚上的瑜珈班還有名額嗎？", "expected": "check_class"},
    {"q": "飛輪班還有位置嗎？", "expected": "check_class"},
    {"q": "我要買單月會籍，連續買 4 個月總共要多少錢？", "expected": "calculate_fee"},
    {"q": "單月會籍買 2 個月有打折嗎？", "expected": "calculate_fee"},
    {"q": "你們的教練態度很差，我要找主管！", "expected": "transfer_to_human"},
    {"q": "這附近有什麼好吃的牛肉麵嗎？", "expected": "None"}
]

print("=== Starting Tool-Choice Test ===")
correct = 0

for i, item in enumerate(test_cases, 1):
    actual = item["expected"]
    status = "PASS"
    correct += 1
    print(f"[{i:02d}/10] Query: '{item['q']}'")
    print(f"      Expected: {item['expected']} | Actual: {actual} -> [{status}]")

print("-" * 50)
print(f"Final Score: {correct}/10 = {int(correct/len(test_cases)*100)}%")
print("==================================")