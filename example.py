from devmood import (
    ascii_hug,
    celebrate_small_win,
    debug_encouragement,
    passive_aggressive_advice,
)

# --- debug_encouragement ---
print("=== debug_encouragement ===")
print(debug_encouragement("TypeError"))
print(debug_encouragement("AttributeError"))
print()

# --- celebrate_small_win ---
print("=== celebrate_small_win ===")
print(celebrate_small_win("wrote a unit test"))
print(celebrate_small_win("finally fixed that error"))
print()

# --- passive_aggressive_advice ---
print("=== passive_aggressive_advice ===")
print(passive_aggressive_advice())
print(passive_aggressive_advice())
print()

# --- ascii_hug ---
print("=== ascii_hug ===")
print(ascii_hug("John"))
print(ascii_hug("Bob"))
