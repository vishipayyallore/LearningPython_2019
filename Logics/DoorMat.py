inputs = list(map(int, input().split()))

row_count = inputs[0]
column_count = inputs[1]

display_data = 'WELCOME'
tower = '.|.'
tower_count = 1
dash = '-'
dash_count = (column_count - 3) // 2

for counter in range(1, (row_count+1)):
    
    if( counter <= row_count//2):
        print(dash*dash_count, end='')
        print(tower*tower_count, end='')
        print(dash*dash_count)
        
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

        print(dash*dash_count, end='')
        print(tower*tower_count, end='')
        print(dash*dash_count)
