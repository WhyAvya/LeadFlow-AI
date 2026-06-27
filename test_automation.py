from automation import *

score, priority = calculate_priority(
    "Wedding",
    500000,
    220
)

print(score)
print(priority)

package = recommend_package(
    "Wedding",
    500000
)

print(package)

message = generate_ai_message(
    "Avya",
    "Wedding",
    220,
    package
)

print()
print(message)