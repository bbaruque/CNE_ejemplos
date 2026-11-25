import gymnasium as gym
# Crear el entorno de CartPole
# env = gym.make('CartPole-v1', render_mode="rgb_array")
env = gym.make('CartPole-v1', render_mode="human")

try:
    for i_episode in range(20):

        observation, info = env.reset()
        recompensa = 0

        for t in range(200):

            #env.render()
            print(observation)
            action = int(input("Pulsa 6 para empujar izquierda (mueve derecha) o 4 para empujar derecha (mueve izquierda): "))

            if action == 6:
                action = 0
                print("Valor ", action, " empuja izquierda (mueve derecha)")
            elif action == 4:
                action = 1
                print("Valor ", action, " empuja derecha (mueve izquierda)")

            observation, reward, terminated, truncated, info = env.step(action)
            recompensa = recompensa + reward

            #input ("Pulsa Enter para continuar")

            if terminated or truncated:
                print("Paso final que provoca el fin del episodio:")
                print(observation)
                print("Episodio ", i_episode, "terminado en {} intentos".format(t + 1))
                print("Recompensa obtenida: ", recompensa)
                break

        input("Fin del episodio, pulsa Enter para continuar")
finally:
    env.close()