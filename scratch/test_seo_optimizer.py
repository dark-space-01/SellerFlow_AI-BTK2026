import os
import sys
# Add parent directory to sys.path so we can import from main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import agent_seo_optimizer

def run_test(niche, tag_strategy, is_design_product):
    print("=" * 60)
    print(f"TESTING: Niche='{niche}', Strategy='{tag_strategy}', DesignProduct={is_design_product}")
    print("=" * 60)
    try:
        res = agent_seo_optimizer(niche, tag_strategy, is_design_product)
        print(f"SUCCESS!")
        print(f"TITLE ({len(res['title'])} chars): {res['title']}")
        print(f"CTR ESTIMATE: {res['ctr_estimate']}")
        print(f"OVERALL SEO SCORE: {res['overall_seo_score']}/100")
        print("\nTAGS (13 total, each <= 20 chars, no special characters):")
        for i, t in enumerate(res["tags"]):
            word = t["word"]
            length = len(word)
            has_special = any(c not in "abcdefghijklmnopqrstuvwxyz0123456789 " for c in word)
            vol = t["search_volume"]
            comp = t["competition"]
            verified = "YES - Etsy Verified" if t["etsy_verified"] else "NO - AI Estimate"
            print(f"  {i+1:2d}. '{word}' ({length:2d} chars) | Vol: {vol:<5} | Comp: {comp:<6} | {verified} | Special: {'WARNING' if has_special else 'None'}")
        
        print("\nDESCRIPTION PREVIEW:")
        desc_lines = res["description"].split("\n")
        for line in desc_lines[:4]:
            print(f"  {line}")
        if len(desc_lines) > 4:
            print("  ...")
            
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
    print("-" * 60)
    print("\n")

if __name__ == "__main__":
    # Test 1: Turkish niche for clothing (Balanced)
    run_test("kedi tişörtü", "balanced", is_design_product=True)
    
    # Test 2: Turkish niche for physical item (High Traffic)
    run_test("ahşap yemek masası", "high_traffic", is_design_product=False)
    
    # Test 3: English niche (Low Competition)
    run_test("cozy mountain cabins retro design", "low_competition", is_design_product=True)
