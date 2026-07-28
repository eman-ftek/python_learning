import json
def analyze_loge(log_filename):
    print("=== Security Log Analysis Report ===")
    failed_attempts = {}
    try:
        with open(log_filename,  "r", encoding="utf-8") as file:
            for line in file:
                if "LOGIN_AFILED" in line or "LOGIN_FAILED" in line:
                    parts = line.strip().split(":")
                    account_no = parts[-1].strip()
                    failed_attempts[account_no] = failed_attempts.get(account_no,0) + 1
        print("\nFailed Login Summary: ")
        blocked_list = []
        for acc, count in failed_attempts.items():
            print(f"- Account [{acc}]: {count} failed attempts")
            if count >= 3:
                print(f" SECURITY WARNING: Possible Brute-Force attack detected on Account {acc}!")
                blocked_list.append(acc)
        if blocked_list:
            with open("blocked_account.json", "w", encoding="utf-8") as block_file:
                json.dump(blocked_list, block_file, indent=4)
            print(f"\n[AUTO-DEFENSE] Blocked Account saved to 'blocked_account.json: ' {blocked_list}")
    except FileNotFoundError:
        print("Error: Log file not found!")
analyze_loge("bank.log")
