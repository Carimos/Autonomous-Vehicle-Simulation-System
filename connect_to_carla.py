import carla

def main():
    try:
        # Connect to the CARLA server
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        world = client.get_world()

        print('Successfully connected to CARLA!')
        print(f'Current map: {world.get_map().name}')

    except Exception as e:
        print('Error connecting to Carla:', e)

if __name__ == '__main__':
    main()