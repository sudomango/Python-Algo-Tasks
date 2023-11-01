# Поменять значения двух переменных, не используя при этом третью (три способа).

var_a = 100
var_b = 200

print(f"var_a = {var_a}, var_b = {var_b}")

# Используем сложение и вычитание, как обратную сложению операцию.

var_a = var_a + var_b
var_b = var_a - var_b
var_a = var_a - var_b

print(f"var_a = {var_a}, var_b = {var_b}")

# Используем распаковку (специальная языковая конструкция).

var_a, var_b = var_b, var_a  # Можно записать ещё как var_a, var_b = (var_b, var_a), то есть использовать Tuple Unpacking.

print(f"var_a = {var_a}, var_b = {var_b}")

# Здесь мы используем побитовое XOR, которое является обратной операцией для самой себя.

var_a = var_a ^ var_b
var_b = var_a ^ var_b
var_a = var_a ^ var_b

print(f"var_a = {var_a}, var_b = {var_b}")