display_data = 'WELCOME'
tower = '.|.'
dash = '-'

def display_matrow(dash_count, tower_count):
    print(dash*dash_count, end='')
    print(tower*tower_count, end='')
    print(dash*dash_count)

def display_doormat(row_count, column_count):
    tower_count = 1
    dash_count = (column_count - 3) // 2

    for counter in range(1, (row_count+1)):
        if(counter <= row_count//2):
            display_matrow(dash_count, tower_count)
            tower_count += 2
            dash_count -= 3
        elif(counter == (row_count//2)+1):
            count = (column_count-len(display_data))//2
            print(dash*count, end='')
            print(display_data, end='')
            print(dash*count)
        else:
            tower_count -= 2
            dash_count += 3
            display_matrow(dash_count, tower_count)

if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    display_doormat(inputs[0], inputs[1])
