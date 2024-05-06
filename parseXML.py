import xml.etree.ElementTree as ET

# Clase base para Address y Item
class XmlElement:
    def __init__(self, element):
        self.element = element

    # Método para obtener el texto de un elemento XML
    def get_element_text(self, tag):
        # Polimorfismo: el método se puede utilizar en subclases para obtener el texto de un elemento XML
        elem = self.element.find(tag)
        return elem.text if elem is not None else None

    # Método para obtener el valor flotante de un elemento XML
    def get_element_float(self, tag):
        # Polimorfismo: el método se puede utilizar en subclases para obtener un valor flotante de un elemento XML
        elem = self.element.find(tag)
        return float(elem.text) if elem is not None else None

# Clase Address que hereda de XmlElement
class Address(XmlElement):
    def __init__(self, element):
        super().__init__(element)

    # Propiedades para obtener los datos de la dirección
    @property
    def name(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener el nombre
        return self.get_element_text('name')

    @property
    def street(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener la calle
        return self.get_element_text('street')

    @property
    def city(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener la ciudad
        return self.get_element_text('city')

    @property
    def zip_code(self):
        # Polimorfismo: se utiliza el método get_element_float de la clase base para obtener el código postal
        return self.get_element_float('zip')

# Clase Item que hereda de XmlElement
class Item(XmlElement):
    def __init__(self, element):
        super().__init__(element)

    # Propiedades para obtener los datos del ítem
    @property
    def product(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener el producto
        return self.get_element_text('product')

    @property
    def quantity(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener la cantidad
        return int(self.get_element_text('quantity'))

    @property
    def price(self):
        # Polimorfismo: se utiliza el método get_element_text de la clase base para obtener el precio
        return float(self.get_element_text('price'))

# Clase PurchaseOrder
class PurchaseOrder:
    def __init__(self, ship_to, bill_to, items, order_date=None, comment=None):
        self.ship_to = ship_to
        self.bill_to = bill_to
        self.items = items
        self.order_date = order_date
        self.comment = comment

# Función para leer el archivo XML y construir los objetos
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Obteniendo elementos de PurchaseOrder
    order_date = root.attrib.get('orderDate')
    ship_to_elem = root.find('shipTo')
    ship_to = Address(ship_to_elem)

    bill_to_elem = root.find('billTo')
    bill_to = Address(bill_to_elem)

    comment_elem = root.find('comment')
    comment = comment_elem.text if comment_elem is not None else None

    # Obteniendo elementos de Items
    items = []
    items_elem = root.find('items')
    for item_elem in items_elem.findall('item'):
        item = Item(item_elem)
        items.append(item)

    # Creando el objeto PurchaseOrder
    purchase_order = PurchaseOrder(ship_to, bill_to, items, order_date, comment)
    return purchase_order

# Función para imprimir la estructura del archivo XML
def print_xml_structure(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print(f"Root element: {root.tag}")
    print("Children:")
    for child in root:
        print(f"  - {child.tag}")

if __name__ == "__main__":
    # Nombre del archivo XML
    xml_file = "ejemplo.xml"

    # Imprimir la estructura del archivo XML
    print("Estructura del archivo XML:")
    print_xml_structure(xml_file)

    # Crear objetos a partir del archivo XML
    print("\nCreando objetos desde el archivo XML:")
    purchase_order = parse_xml(xml_file)
    print(f"Fecha de orden: {purchase_order.order_date}")
    print(f"Comentario: {purchase_order.comment}")
    print("Dirección de envío:")
    print(f"  Nombre: {purchase_order.ship_to.name}")
    print(f"  Calle: {purchase_order.ship_to.street}")
    print(f"  Ciudad: {purchase_order.ship_to.city}")
    print(f"  Código postal: {purchase_order.ship_to.zip_code}")
    print("Dirección de facturación:")
    print(f"  Nombre: {purchase_order.bill_to.name}")
    print(f"  Calle: {purchase_order.bill_to.street}")
    print(f"  Ciudad: {purchase_order.bill_to.city}")
    print(f"  Código postal: {purchase_order.bill_to.zip_code}")
    print("Ítems:")
    for i, item in enumerate(purchase_order.items, 1):
        print(f"  Item {i}:")
        print(f"    Producto: {item.product}")
        print(f"    Cantidad: {item.quantity}")
        print(f"    Precio: ${item.price}")
