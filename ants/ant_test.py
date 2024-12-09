from ants import *
from ants import Hive, AssaultPlan, dry_layout, GameState, ant_types, Bee, FireAnt

# 创建蜂巢和布局
beehive, layout = Hive(AssaultPlan()), dry_layout

# 设置游戏尺寸
dimensions = (1, 9)

# 创建游戏状态
gamestate = GameState(beehive, ant_types(), layout, dimensions)

# 测试代码
place = gamestate.places['tunnel_0_4']
bee = Bee(10)
ant = FireAnt(1)

# 将 Bee 和 FireAnt 添加到 place
place.add_insect(bee)
place.add_insect(ant)

# # 执行 Bee 的动作，攻击 FireAnt
# bee.action(gamestate)
# print(f"Bee 的生命值（第一次攻击后）: {bee.health}")
# print(f"FireAnt 的生命值（第一次攻击后）: {ant.health}")
# print(f"FireAnt 是否已经死亡: {place.ant is None}")
# print(f"Bee 的位置（第一次攻击后）: {bee.place.name}")


# # 检查 Bee 的生命值
# bee_health_after_attack = bee.health

# # 检查 FireAnt 的生命值
# ant_health_after_attack = ant.health

# # 检查 FireAnt 是否已经死亡
# is_ant_dead = place.ant is None

# # 再次执行 Bee 的动作，检查 Bee 是否被阻挡
# bee.action(gamestate)

# # 检查 Bee 的生命值是否未变
# bee_health_after_second_attack = bee.health

# # 检查 Bee 的位置是否未变
# bee_place_after_attack = bee.place.name

# print(f"Bee 的生命值（第一次攻击后）: {bee_health_after_attack}")
# print(f"FireAnt 的生命值（第一次攻击后）: {ant_health_after_attack}")
# print(f"FireAnt 是否已经死亡: {is_ant_dead}")
# print(f"Bee 的生命值（第二次攻击后）: {bee_health_after_second_attack}")
# print(f"Bee 的位置（第二次攻击后）: {bee_place_after_attack}")

