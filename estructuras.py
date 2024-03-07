#objetos o diccionarios
clienteUno={
    "id":5,
    "nombre":"edif1",
    "consumo":200,
    
}
clientedos={
    "id":6,
    "nombre":"edif2",
    "consumo":500,
    
}
#se declara una  lista o arreglos

clientesAsociados=[clienteUno, clientedos]

#obtener imformacion dela lista
#print(len(clientesAsociados)) para saber cuantos objetos  hay en la lista
#print(type(clientesAsociados))  para saber el tipo de dato que es

#for  i in range(len(clientesAsociados)):   #este bucle recorre los elementos de la lista
   # print("Cliente: ",i+1)

'''for i in range (2):
    print(clientesAsociados[i]["consumo"])'''#esto solo muestra los consumos pero no las claves y su respectivo valor
    
#foreach que es un for expecializado en recorrerarreglos
for cliente in clientesAsociados:
    print (cliente['id'],'=>',cliente ['consumo'],'kwh')
    print(f"{cliente['id']}=>{cliente['consumo']}kwh")
    