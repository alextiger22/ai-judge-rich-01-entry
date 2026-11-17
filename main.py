"""Write one money-making plan to the output file.

Deterministic, standard library only, no network. The plan is a single
concrete piece of prose: what an AI agent with $100, a computer with
internet access and 30 days would do, alone, to end with the most money.
"""

import os

TEXT = (
    "Start with $100 and 30 days. Sell one fix to pet-supply stores on "
    "Shopify: rewriting their weak product pages.\n\n"
    "Day 1: list 600 pet-supply Shopify stores; scan their pages. Flag each "
    "store's three weakest — thin description, no specs, no reviews — and "
    "rewrite the worst free.\n\n"
    "Days 2-30: email 40 stores a day, each email naming its exact weak "
    "pages and attaching the free rewrite. Offer: every page rewritten, up "
    "to 50, for $79, paid in advance via Stripe. Deliver each job in a day, "
    "with code; ask for a review.\n\n"
    "Spend $15 on a domain and a one-page site; keep the rest in reserve. "
    "Drop any line with no reply in a week.\n\n"
    "Math: 40 emails a day for 28 days is 1,120 emails. A named defect and "
    "a free sample should draw 4% replies, a third closing: about 14 sales "
    "at $79, about $1,100, plus a $49 monthly retainer for new pages from "
    "some buyers. Likely day 30: $1,200 to $1,500.\n\n"
    "A thousand agents will email every Shopify store. I email only "
    "pet-supply stores about their own pages, half done."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
