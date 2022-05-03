def cube_element_1():
    print('+ - - - - + - - - - +')

def cube_element_2():
    print('|',' '*7,'|',' '*7,'|')

def print_element_2():
    cube_element_2()
    cube_element_2()
    cube_element_2()
    cube_element_2()

def print_cube():
    cube_element_1()
    print_element_2()
    cube_element_1()
    print_element_2()
    cube_element_1()


def cube2_element_1_initial():
    print(f'+',f'-'*4,'+','-' *4,'+','-' *4,'+','-' *4,'+')

def cube2_element_2_initial():
    print('|',' '*4,'|',' '*4,'|',' '*4,'|',' '*4,'|')


def cube2_block1():
    cube2_element_1_initial()
    cube2_element_2_initial()
    cube2_element_2_initial()

def cube2_print():
    cube2_block1()
    cube2_block1()
    cube2_block1()
    cube2_block1()
    cube2_element_1_initial()


cube2_print()