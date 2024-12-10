from ants import *
from ants import Hive, AssaultPlan, dry_layout, GameState, ant_types, LaserAnt, HarvesterAnt, Bee

# 创建蜂巢和布局
beehive, layout = Hive(AssaultPlan()), dry_layout

# 设置游戏尺寸
dimensions = (1, 9)

# 创建游戏状态
gamestate = GameState(beehive, ant_types(), layout, dimensions)

# # 测试代码
# laser = LaserAnt()
# ant = HarvesterAnt(2)
# bee1 = Bee(2)
# bee2 = Bee(2)
# bee3 = Bee(2)
# bee4 = Bee(2)

# # 将 LaserAnt、Bee 和 HarvesterAnt 添加到相应的位置
# gamestate.places["tunnel_0_0"].add_insect(laser)
# gamestate.places["tunnel_0_0"].add_insect(bee4)
# gamestate.places["tunnel_0_3"].add_insect(bee1)
# gamestate.places["tunnel_0_3"].add_insect(bee2)
# gamestate.places["tunnel_0_4"].add_insect(ant)
# gamestate.places["tunnel_0_5"].add_insect(bee3)


# # 创建蜂巢和布局
# beehive, layout = Hive(AssaultPlan()), dry_layout

# # 设置游戏尺寸
# dimensions = (1, 9)

# # 创建游戏状态
# gamestate = GameState(beehive, ant_types(), layout, dimensions)

# # 测试代码
laser = LaserAnt()
container_laser = TankAnt()
bee2 = Bee(3)
harvester_ant = HarvesterAnt(3)
container_ant = BodyguardAnt()
bee3 = Bee(4)

# 将 LaserAnt、TankAnt、Bee 和 HarvesterAnt 添加到相应的位置
gamestate.places["tunnel_0_0"].add_insect(laser)
gamestate.places["tunnel_0_0"].add_insect(container_laser)
gamestate.places["tunnel_0_2"].add_insect(bee2)
gamestate.places["tunnel_0_8"].add_insect(harvester_ant)
gamestate.places["tunnel_0_8"].add_insect(container_ant)
gamestate.places["tunnel_0_8"].add_insect(bee3)

# # 执行 LaserAnt 的动作
# laser.action(gamestate)

# # 检查 Bee2 的生命值
# bee2_health_after_attack = bee2.health

# # 检查 HarvesterAnt 的生命值
# harvester_health_after_attack = harvester_ant.health

# # 检查 ContainerAnt 的生命值
# container_health_after_attack = container_ant.health

# # 检查 Bee3 的生命值
# bee3_health_after_attack = bee3.health

# # 检查 LaserAnt 的生命值
# laser_health_after_attack = laser.health

# # 检查 ContainerLaser 的生命值
# container_laser_health_after_attack = container_laser.health

# print(f"Bee2 的生命值（攻击后）: {bee2_health_after_attack}")
# print(f"HarvesterAnt 的生命值（攻击后）: {harvester_health_after_attack}")
# print(f"ContainerAnt 的生命值（攻击后）: {container_health_after_attack}")
# print(f"Bee3 的生命值（攻击后）: {bee3_health_after_attack}")
# print(f"LaserAnt 的生命值（攻击后）: {laser_health_after_attack}")
# print(f"ContainerLaser 的生命值（攻击后）: {container_laser_health_after_attack}")
