# ------------------------------- VARIABLES ---------------------------------------------------
# ----- almacenamiento------

# ----- estudiantes -------
students = []
set_of_students_id = []

# ----- notas --------------
best_students_and_average = []


# ----- materias -------
subjects = []
set_of_subjects_id = []


# ------------------------------- MENU GENERAL --------------------------------------------------------
def general_menu():
    print('''
        ----------------------------------------------
                        MENÚ PRINCIPAL
        ----------------------------------------------
            1. Gestión de Estudiantes
            2. Gestión de Materias
            3. Asignaciones (Estudiante ↔ Materias)
            4. Notas y Calificaciones
            5. Reportes y Estadísticas
            6. Salir
    ''')

    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option


# ------------------------------- MENU PARA GESTION ESTUDIANTES --------------------------------
def general_manage_students():
    print('''
        ----------------------------------------------
                MENU PARA GESTION ESTUDIANTES
        ----------------------------------------------
            1. Registrar estudiante
            2. Listar estudiantes
            3. Consultar estudiante por ID
            4. Eliminar estudiante
            5. Volver al menú principal
    ''')
    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option
# ------------------------------- FUNCIONES PARA GESTION ESTUDIANTES  ------------------------------
def register_students():
    print('''
        ----------------------------------------------
         PORFAVOR INGRESA LOS DATOS CORRESPONDIENTES
        ---------------------------------------------- ''')
    name = input("Dame tu nombre: \n").lower()
    while True:
        try:
            age = int(input("Dame tu edad: \n"))
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA TU EDAD EN NÚMERO
        ---------------------------------------------- 
            ''')
    while True:
        try:
            id = int(input("Dame tu ID, sin puntos ni comas: \n"))
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA TU ID EN NÚMERO
                   SIN PUNTOS NI COMAS
        ---------------------------------------------- 
            ''')

    if id in set_of_students_id:
        print(f'''
        ----------------------------------------------
          YA HAY UN ESTUDIANTE REGISTRADO CON ESE ID
        ---------------------------------------------- 
            ''')
        return manage_students()
    else:
        set_of_students_id.append(id)
        student = {
            "nombre" : name, 
            "edad": age,
            "id": id,
            "materias" : []
        }

        students.append(student)
        print(f'''
            ----------------------------------------------
                ESTUDIANTE {name.upper()} REGISTRAD@ CON EXITO
            ---------------------------------------------- 
                ''')
        return manage_students()

def list_students():
    if not students:
        print('''
        ----------------------------------------------
                 NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return manage_students()
    
    if not students:
        print('''
        ----------------------------------------------
                 NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return manage_students()

    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}
            EDAD:   {students[i]['edad']}
            IDENTIFICACION: {students[i]['id']}
        ----------------------------------------------    
        ''')
    print()
    return manage_students()

def consult_student():
    if not students:
        print('''
        ----------------------------------------------
                 NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return manage_students()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}
        ----------------------------------------------    
        ''')

    while True:
        try:
            option = int(input("Ingresa el ID del estudiante que quieres consultar: \n"))
            value = students[option]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
        
    print(f'''
        ----------------------------------------------
                 INFORMACIÓN DEL ESTUDIANTE
        ----------------------------------------------            
            ''')
        
    print(f'''
        ----------------------------------------------
            ID:     {option}
            NOMBRE: {value['nombre'].upper()}
            EDAD:   {value['edad']}
            IDENTIFICACION: {value['id']}
        ----------------------------------------------    
        ''')

    return manage_students()

def remove_student():
    if not students:
        print('''
        ----------------------------------------------
                 NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return manage_students()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}
        ----------------------------------------------    
        ''')

    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante que quieres borrar: \n"))
            value = students[student_id]

            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    
    index_id = set_of_students_id.index(students[student_id]['id'])
    set_of_students_id.pop(index_id)
    
    for i in subjects:
        if student_id in i['estudiantes']:
            index = i['estudiantes'].index(student_id)
            i['estudiantes'].pop(index)
            continue
        else:
            continue

    students.pop(student_id)
    print(f'''
        ----------------------------------------------
            INFORMACIÓN DEL ESTUDIANTE ELIMINADO
        ----------------------------------------------            
            ''')
    print(f'''
        ----------------------------------------------
            ID:     {student_id}
            NOMBRE: {value['nombre'].upper()}
            EDAD:   {value['edad']}
            IDENTIFICACION: {value['id']}
        ----------------------------------------------    
        ''')
    print(f'''
        ----------------------------------------------
             ESTUDIANTE ELIMINADO CORRECTAMENTE
        ----------------------------------------------            
            ''')
    return manage_students()   


# ------------------------------- MENU PARA GESTION MATERIAS --------------------------------
def general_manage_subjects():
    print('''
        ----------------------------------------------
                MENU PARA GESTION MATERIAS
        ----------------------------------------------
            1. Registrar nueva materia
            2. Listar materias
            3. Consultar materia
            4. Eliminar materia
            5. Volver al menú principal
    ''')

    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option
# ------------------------------- FUNCIONES PARA GESTION MATERIAS  ------------------------------
def register_subject():
    print('''
        ----------------------------------------------
         PORFAVOR INGRESA LOS DATOS CORRESPONDIENTES
        ---------------------------------------------- ''')
    subject = input("Ingresa el nombre de la materia: \n")
    if subject in set_of_subjects_id:
        print(f'''
        ----------------------------------------------
        LA MATERIA {subject.upper()} YA SE ENCUENTRÁ REGISTRADA
        ---------------------------------------------- 
            ''')
        return manage_subjects()
    else:
        set_of_subjects_id.append(subject)
        subject_items = {
            'materia': subject,
            'estudiantes': []
        }
        subjects.append(subject_items)

    print(f'''
        ----------------------------------------------
         MATERIA {subject.upper()} REGISTRADA CON EXITO
        ---------------------------------------------- 
                ''')
    return manage_subjects()

def list_subjects():
    if not subjects:
        print('''
        ----------------------------------------------
                  NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return manage_subjects()
    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(subjects)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
            MATERIA: {subjects[i]['materia'].upper()}
        ----------------------------------------------    
        ''')
    print()
    return manage_subjects()

def consult_subject():
    if not subjects:
        print('''
        ----------------------------------------------
                    NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return manage_subjects()
    

    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(subjects)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
        ----------------------------------------------    
        ''')
    print()

    while True:
        try:
            option = int(input("Ingresa el ID de la materia que quieres consultar: \n"))
            value = subjects[option]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
        
    print(f'''
        ----------------------------------------------
                  INFORMACIÓN DE LA MATERIA
        ----------------------------------------------            
            ''')
        
    print(f'''
        ----------------------------------------------
            ID:     {option}
            MATERIA: {value['materia'].upper()}
        ----------------------------------------------    
        ''')

    return manage_subjects()

def remove_subject():
    if not subjects:
        print('''
        ----------------------------------------------
                  NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return manage_subjects()
    
    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(subjects)):
        print(f'''
        ----------------------------------------------
            ID:     {i}
        ----------------------------------------------    
        ''')
    print()

    while True:
        try:
            subject_id = int(input("Ingresa el ID de la materia que quieres borrar: \n"))
            value = subjects[subject_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    index_id = set_of_subjects_id.index(subjects[subject_id]['materia'])
    set_of_subjects_id.pop(index_id)
    
    for i in students:
        if subject_id in i['materias']:
            index = i['materias'].index(subject_id)
            i['materias'].pop(index)
            i.pop(subject_id)
            continue
        else:
            continue

    subjects.pop(subject_id)

    print(f'''
        ----------------------------------------------
            INFORMACIÓN DE LA MATERIA ELIMINADA
        ----------------------------------------------            
            ''')
    print(f'''
        ----------------------------------------------
            ID:     {subject_id}
            MATERIA: {value['materia']}
        ----------------------------------------------    
        ''')
    print(f'''
        ----------------------------------------------
               MATERIA ELIMINADA CORRECTAMENTE
        ----------------------------------------------            
            ''')
    return manage_subjects()   


# ------------------------------- MENU DE ASIGNACIÓN MATERIAS --------------------------------
def general_assign_subject_to_students():
    print('''
        ----------------------------------------------
                MENU PARA ASIGNAR MATERIAS
        ----------------------------------------------
            1. Asignar materia a estudiante
            2. Ver materias de un estudiante
            3. Ver estudiantes por materia
            4. Quitar materia a un estudiante
            5. Volver al menú principal
    ''')

    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option
# ------------------------------- FUNCIONES DE ASIGNACIÓN MATERIAS  ------------------------------
def assign_subject_to_students():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()

   
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para asignación de matería: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')


    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(subjects)):
        print(f'''
            ID:     {i}
            MATERIA: {subjects[i]['materia'].upper()} 
        ''')

    while True:
        try:
            subject_id = int(input("Ingresa el ID de la matería: \n"))
            value_subject = subjects[subject_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    # evaluar students & subjects
    if subject_id in students[student_id]['materias'] or student_id in subjects[subject_id]['estudiantes']:
        print(f'''
        ----------------------------------------------
            ESTUDIANTE {value_student['nombre'].upper()} 
            YA TIENE LA MATERIA {value_subject['materia'].upper()}
                            REGISTRADA!!
        ---------------------------------------------- ''')
        return assign_subject()
    else:
        subjects[subject_id]['estudiantes'].append(student_id)
        students[student_id]['materias'].append(subject_id)
        # crear materia key y value []
        students[student_id][subject_id] = []

    print(f'''
        ----------------------------------------------
            ESTUDIANTE {value_student['nombre'].upper()} 
            HA REGISTRADO LA MATERIA {value_subject['materia'].upper()}
                        ¡¡CORRECTAMENTE!!
        ---------------------------------------------- ''')
    return assign_subject()

def subjects_per_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    
    print('''
        ----------------------------------------------
                   MATERIAS POR ESTUDIANTE
        ---------------------------------------------- 
            ''')
    for i in range(len(students)):
        print(f'''
        ----------------------------------------------
                        ESTUDIANTE
        ----------------------------------------------
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}
            EDAD:   {students[i]['edad']}
            IDENTIFICACION: {students[i]['id']}
 
        ''')
        print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        for j in students[i]['materias']:
            print(f'''
            ID: {j}
            MATERIA: {subjects[j]['materia'].upper()}   
        ''')
    print('''
        ---------------------------------------------- ''')         
    return assign_subject()

def students_per_subject():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    
    print('''
        ----------------------------------------------
                   ESTUDIANTES POR MATERIA  
        ---------------------------------------------- 
            ''')
    for i in range(len(subjects)):
        print(f'''
        ----------------------------------------------
                          MATERIA
        ----------------------------------------------
            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}  
        ''')
        print('''
        ----------------------------------------------
                    ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        for j in subjects[i]['estudiantes']:
            print(f'''
            ID:     {j}
            NOMBRE: {students[j]['nombre'].upper()}
            EDAD:   {students[j]['edad']}
            IDENTIFICACION: {students[j]['id']}
        ''')
    print('''
        ---------------------------------------------- ''')        
    return assign_subject()
    
def remove_subject_to_a_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return assign_subject()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para RETIRAR materia: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    
    if not students[student_id]['materias']:
        print('''
        ----------------------------------------------
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
        ''')
        return assign_subject()

    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')   
    for i in students[student_id]['materias']:
        print(f'''
            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}   
        ''')
    print('''
        ---------------------------------------------- ''')

    while True:
        try:
            subject_id = int(input("Ingresa el ID de la matería a RETIRAR: \n"))
            value = subjects[subject_id]['materia']
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')  

    while True:
        try:
            advice = int(input(f'''
        ----------------------------------------------
                Vas a eliminar la materia {value.upper()}
                Del estudiante {students[student_id]['nombre'].upper()}

                    ESTAS SEGURO:

                        1: SI
                        2: NO
        ----------------------------------------------\n'''))
            if advice == 1 or advice == 2:
                break
            else:
                raise Exception
        except:
            print('''
        ----------------------------------------------
                  INGRESA 1: SI O 2: NO
        ---------------------------------------------- 
            ''') 
        
    if advice == 1: 
        subject_index = students[student_id]['materias'].index(subject_id)
        students[student_id]['materias'].pop(subject_index)
        students[student_id].pop(subject_id)

        student_index = subjects[subject_id]['estudiantes'].index(student_id)
        subjects[subject_id]['estudiantes'].pop(student_index)

        print('''
        ----------------------------------------------
            SE HA REMOVIDO CORRECTAMENTE LA MATERIA 
        ---------------------------------------------- 
            ''')
        print(f'''
        ----------------------------------------------
                        ESTUDIANTE
        ----------------------------------------------
            ID:     {student_id}
            NOMBRE: {students[student_id]['nombre'].upper()}
            EDAD:   {students[student_id]['edad']}
            IDENTIFICACION: {students[student_id]['id']}
    
            ''')
        print('''
        ----------------------------------------------
                   MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        for j in students[student_id]['materias']:
                print(f'''
                ID: {j}
                MATERIA: {subjects[j]['materia'].upper()}   
            ''')
        print('''
        ---------------------------------------------- ''')       
    else:
        print('''
        ----------------------------------------------
                    TRANSACCION INTERRUMPIDA
        ---------------------------------------------- 
            ''') 
        return assign_subject()  
           
    return assign_subject()


# ------------------------------- MENU DE NOTAS Y CALIFICACIONES ---------------------------------
def general_notes_and_grades():
    print('''
        ----------------------------------------------
               MENU PARA NOTAS Y CALIFICACIONES
        ----------------------------------------------
            1. Registrar nota para un estudiante
            2. Ver notas por materia
            3. Ver promedio de un estudiante
            4. Eliminar una nota
            5. Volver al menú principal
        ''')
    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option
# ------------------------------- FUNCIONES DE NOTAS Y CALIFICACIONES  ------------------------------
def register_note_per_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para CALIFICAR: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
        
    if not students[student_id]['materias']:
        print('''
        ----------------------------------------------
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
        ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in students[student_id]['materias']:
        print(f'''
            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}   
        ''')
    print('''
        ---------------------------------------------- ''')
    while True:
        try:
            subject_id = int(input("Ingresa el ID de la matería a CALIFICAR: \n"))
            value_subject = subjects[subject_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    
    while True:
        try:
            note = float(input(f"Ingresa la nota a registrar en {value_subject['materia'].upper()}:\n"))
            if note >= 0.0 and note <= 5.0:
                break
            else:
                raise Exception
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN UNA NOTA VALIDA
                      ENTRE 0.0 Y 5.0
        ---------------------------------------------- 
            ''')
    
    students[student_id][subject_id].append(note)
    print(f'''
        ----------------------------------------------
                        ESTUDIANTE
        ----------------------------------------------
            ID:     {student_id}
            NOMBRE: {students[student_id]['nombre'].upper()}
            EDAD:   {students[student_id]['edad']}
            IDENTIFICACION: {students[student_id]['id']}

            MATERIA: {subjects[subject_id]['materia'].upper()}
            NOTAS:   {students[student_id][subject_id]}   
        ''')
    print('''
        ----------------------------------------------
                NOTA REGISTRADA CON EXITO
        ---------------------------------------------- 
            ''')
    return notes_and_grades()

def notes_per_subject():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para VER CALIFICACIONES: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
        
    if not students[student_id]['materias']:
        print('''
        ----------------------------------------------
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
        ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                MATERIAS Y NOTAS REGISTRADAS
        ---------------------------------------------- ''')
    for i in students[student_id]['materias']:
        print(f'''
            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}
            NOTAS:   {value_student[i]}
        ''')
    print('''
        ---------------------------------------------- ''')
    
    return notes_and_grades()

def average_per_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para VER CALIFICACIONES: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
        
    if not students[student_id]['materias']:
        print('''
        ----------------------------------------------
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
        ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                MATERIAS Y NOTAS REGISTRADAS
        ---------------------------------------------- ''')

    for i in students[student_id]['materias']:
        average = 0
        print(f'''
            ID_ESTUDIANTE: {student_id}
            ESTUDIANTE: {value_student['nombre'].upper()}

            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}
            NOTAS:   {value_student[i]}''')
        
        for j in value_student[i]:
            average += j
        print(f'''
            PROMEDIO: {average/ len(value_student[i])}
        ---------------------------------------------- ''') 
    print('''
        ---------------------------------------------- ''')
    
    return notes_and_grades()

def remove_note():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
        return notes_and_grades()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
    while True:
        try:
            student_id = int(input("Ingresa el ID del estudiante para RETIRAR NOTA: \n"))
            value_student = students[student_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    
    if not students[student_id]['materias']:
        print('''
        ----------------------------------------------
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
        ''')
        return notes_and_grades()
 
    print('''
        ----------------------------------------------
                     MATERIAS REGISTRADOS
        ---------------------------------------------- ''')
    for i in students[student_id]['materias']:
        print(f'''
            ID: {i}
            MATERIA: {subjects[i]['materia'].upper()}   
        ''')
    print('''
        ---------------------------------------------- ''')

    while True:
        try:
            subject_id = int(input("Ingresa el ID de la matería a RETIRAR NOTA: \n"))
            subject_value = subjects[subject_id]['materia']
            break
        except:
            print('''
        ----------------------------------------------
             POR FAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')
    
    print(f'''
        ----------------------------------------------
                          NOTAS
        ---------------------------------------------- 
        
            ID: {subject_id}
            MATERIA: {subjects[subject_id]['materia'].upper()}
          ''')
    for i in range(len(students[student_id][subject_id])):
        print(f'''
            NOTA_ID: {i}
            NOTAS:  {students[student_id][subject_id][i]}
        ''')
    print('''
        ---------------------------------------------- ''')  
    while True:
        try:
            note_id = int(input("Ingresa el ID de la NOTA a RETIRAR: \n"))
            note_value = students[student_id][subject_id][note_id]
            break
        except:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN ID CORRECTO
        ---------------------------------------------- 
            ''')

    while True:
        try:
            advice = int(input(f'''
        ----------------------------------------------
              Vas a eliminar una nota de {subject_value.upper()}
                Del estudiante {students[student_id]['nombre'].upper()}

                    ESTAS SEGURO:

                        1: SI
                        2: NO
        ----------------------------------------------\n'''))
            if advice == 1 or advice == 2:
                break
            else:
                raise Exception
        except:
            print('''
        ----------------------------------------------
                  INGRESA 1: SI O 2: NO
        ---------------------------------------------- 
            ''') 
        
    if advice == 1: 
        students[student_id][subject_id].pop(note_id)
        print('''
        ----------------------------------------------
            SE HA REMOVIDO CORRECTAMENTE LA NOTA 
        ---------------------------------------------- 
            ''')
        print(f'''
        ----------------------------------------------
                        ESTUDIANTE
        ----------------------------------------------
            ID:     {student_id}
            NOMBRE: {students[student_id]['nombre'].upper()}
            EDAD:   {students[student_id]['edad']}
            IDENTIFICACION: {students[student_id]['id']}

            MATERIA MODICICADA: {subject_value.upper()}
            NOTAS: {students[student_id][subject_id]}

            NOTA ELIMINADA: {note_value}
    
            ''')     
    else:
        print('''
        ----------------------------------------------
                    TRANSACCION INTERRUMPIDA
        ---------------------------------------------- 
            ''') 
        return notes_and_grades()  
           
    return notes_and_grades()


# ------------------------------- MENU DE REPORTES Y ESTADISTICA ---------------------------------
def general_reports_and_statistics():
    print('''
        ----------------------------------------------
                 MENU PARA ASIGNAR MATERIAS
        ----------------------------------------------
            1. Promedios detallados por estudiante
            2. Estudiante con mejor promedio
            3. Porcentaje de aprobación del grupo
            4. Promedio general del grupo
            5. Ranking de estudiantes
            6. Volver al menú principal
        ''')
    while True:
        try:
            option = int(input("Seleccione una opción: \n"))
            break
        except:
            print('''
        ----------------------------------------------
                INGRESA SOLO UN VALOR NUMERICO
        ---------------------------------------------- ''')
    return option
# ------------------------------- FUNCIONES DE REPORTES Y ESTADISTICA  ------------------------------
def details_average_per_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADAS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    
    print('''
        ----------------------------------------------
                  ESTUDIANTE REGISTRAD@
        ---------------------------------------------- ''')
    for i in range(len(students)):
        print(f'''
            ID:     {i}
            NOMBRE: {students[i]['nombre'].upper()}  
        ''')
        if not students[i]['materias']:
            print('''
         EL ESTUDIANTE NO TIENE MATERIAS REGISTRADAS
        ---------------------------------------------- 
            ''')
        else:
            print('''
                  MATERIAS Y NOTAS REGISTRADAS
        ---------------------------------------------- ''')
            for j in students[i]['materias']:
                average = 0
                print(f'''
            ID: {j}
            MATERIA: {subjects[j]['materia'].upper()}
            NOTAS:   {students[i][j]}''')
                
                for m in students[i][j]:
                    average += m
                    size = 1 if len(students[i][j]) < 1 else len(students[i][j])
                print(f'''
            PROMEDIO: {average/ size}
        ---------------------------------------------- ''') 
            print('''
        ---------------------------------------------- ''')
    
    return reports_and_statistics()

def best_average_student():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADAS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    
    best_students_and_average.clear()
    for i in range(len(students)):
        if not students[i]['materias']:
            continue

        else:
            for j in students[i]['materias']:
                size = 1 if len(students[i][j]) < 1 else len(students[i][j])
                average = sum(students[i][j]) / size
                

            target = "Pasa la materia" if average > 3.0 else "No pasa la materia"
            best_students_and_average.append((i,j,average,target))

            best_students_and_average.sort(key=lambda x: x[2], reverse=True)
    
        # obtención de datos
    id_student = best_students_and_average[0][0]
    id_subject = best_students_and_average[0][1]
    student_value = students[best_students_and_average[0][0]]
    subject_value = subjects[best_students_and_average[0][1]]
    max_average = best_students_and_average[0][2]

    print('''
        ----------------------------------------------
                ESTUDIANTE CON MEJOR PROMEDIO
        ---------------------------------------------- ''')
    print(f'''
            ID_ESTUDIANTE:     {id_student}
            NOMBRE: {student_value['nombre'].upper()}

            ID_MATERIA: {id_subject}
            MATERIA: {subject_value['materia'].upper()}
            PROMEDIO: {max_average}
        ----------------------------------------------''')           
    return reports_and_statistics()

def approval_group_percent():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADAS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    
    best_students_and_average.clear()
    for i in range(len(students)):
        if not students[i]['materias']:
            continue

        else:
            for j in students[i]['materias']:
                size = 1 if len(students[i][j]) < 1 else len(students[i][j])
                average = sum(students[i][j]) / size
                
            target = "Pasa la materia" if average > 3.0 else "No pasa la materia"
            best_students_and_average.append((i,j,average,target))

            best_students_and_average.sort(key=lambda x: x[2], reverse=True)

    for id_student, id_subject, avg, targ in best_students_and_average:
    # obtención de datos
        student_value = students[id_student]
        subject_value = subjects[id_subject]

        print('''
        ----------------------------------------------
               ESTUDIANTE, PROMEDIO Y RESULTADO
        ---------------------------------------------- ''')
        print(f'''
            ID_ESTUDIANTE:     {id_student}
            NOMBRE: {student_value['nombre'].upper()}

            ID_MATERIA: {id_subject}
            MATERIA: {subject_value['materia'].upper()}
            PROMEDIO: {avg}

            PASA O NO: {targ}
        ----------------------------------------------''')           
    return reports_and_statistics()

def general_group_average():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADAS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    
    best_students_and_average.clear()
    for i in range(len(students)):
        if not students[i]['materias']:
            continue

        else:
            best_average = 0
            for j in students[i]['materias']:
                size = 1 if len(students[i][j]) < 1 else len(students[i][j])
                average = sum(students[i][j]) / size
                
            target = "Pasa la materia" if average > 3.0 else "No pasa la materia"
            best_students_and_average.append((i,j,average,target))

            best_students_and_average.sort(key=lambda x: x[2], reverse=True)

            total_average = 0

    for id_student, id_subject, avg, targ in best_students_and_average:
        # obtención de datos
        total_average += avg

    target = "Pasa todo el grupo" if total_average > 3.0 else "No pasa todo el grupo"
    print(f'''
        ----------------------------------------------
            PROMEDIO GENERAL : {total_average / len(best_students_and_average)}
            PASAN O NO PASAN: {target}
        ----------------------------------------------''')           
    return reports_and_statistics()

def students_ranking():
    if not students:
        print('''
        ----------------------------------------------
                  NO ESTUDIANTES REGISTRADOS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    if not subjects:
        print('''
        ----------------------------------------------
                   NO MATERIAS REGISTRADAS
        ---------------------------------------------- ''')
        return reports_and_statistics()
    
    best_students_and_average.clear()
    for i in range(len(students)):
        if not students[i]['materias']:
            continue

        else:
            for j in students[i]['materias']:
                size = 1 if len(students[i][j]) < 1 else len(students[i][j])
                average = sum(students[i][j]) / size
                

            target = "Pasa la materia" if average > 3.0 else "No pasa la materia"
            best_students_and_average.append((i,j,average,target))

            best_students_and_average.sort(key=lambda x: x[2], reverse=True)
    i = 1
    for id_student, id_subject, avg, targ in best_students_and_average:
        # obtención de datos
        student_value = students[id_student]
        subject_value = subjects[id_subject]

        if i <= 3 or len(best_students_and_average) <3:

            print(f'''
        ----------------------------------------------
             RANKING MEJOR ESTUDIANTE PUESTO {i}
        ---------------------------------------------- ''')
            print(f'''
            ID_ESTUDIANTE:     {id_student}
            NOMBRE: {student_value['nombre'].upper()}

            ID_MATERIA: {id_subject}
            MATERIA: {subject_value['materia'].upper()}
            PROMEDIO: {avg}
        ----------------------------------------------''')
        i += 1
    return reports_and_statistics()


# ---------------------------- FUNCIONES PRINCIPALES ---------------------------------------------
def manage_students():
    select = general_manage_students()

    match select:
        case 1:
            register_students()
        case 2:
            list_students()
        case 3:
            consult_student()
        case 4:
            remove_student()
        case 5:
            return main()
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return manage_students()            

def manage_subjects():
    select = general_manage_subjects()

    match select:
        case 1:
            register_subject()
        case 2:
            list_subjects()
        case 3:
            consult_subject()
        case 4:
            remove_subject()
        case 5:
            return main()
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return manage_subjects()
   
def assign_subject():
    select = general_assign_subject_to_students()

    match select:
        case 1:
            assign_subject_to_students()
        case 2:
            subjects_per_student()
        case 3:
            students_per_subject()
        case 4:
            remove_subject_to_a_student()
        case 5:
            return main()
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return assign_subject()

def notes_and_grades():
    select = general_notes_and_grades()

    match select:
        case 1:
            register_note_per_student()
        case 2:
            notes_per_subject()
        case 3:
            average_per_student()
        case 4:
            remove_note()
        case 5:
            return main()
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return notes_and_grades()

def reports_and_statistics():
    select = general_reports_and_statistics()

    match select:
        case 1:
            details_average_per_student()
        case 2:
            best_average_student()
        case 3:
            approval_group_percent()
        case 4:
            general_group_average()
        case 5:
            students_ranking()
        case 6:
            return main()
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return reports_and_statistics()



# --------------------------------------- MAIN --------------------------------------
def main():
    select = general_menu()

    match select:
        case 1:
            manage_students()
        case 2:
            manage_subjects()
        case 3:
            assign_subject()
        case 4:
            notes_and_grades()
        case 5:
            reports_and_statistics()
        case 6:
            print('''
        ----------------------------------------------
                   FUE UN PLACER AYUDARTE
        ---------------------------------------------- ''')
            return
        case _:
            print('''
        ----------------------------------------------
             PORFAVOR INGRESA UN VALOR CORRECTO
        ---------------------------------------------- ''')
            return main()

# ------------------------------- INICIO DE LA APP -----------------------------
main()