
import chemhelper

element = "Be"

# Молярная масса элемента:
molar_mass = chemhelper.getMolarMass(element)

# Название элемента:
name = chemhelper.getName(element)

# Атомный номер элемента:
atomic_number = chemhelper.getAtomicNumber(element)

# Полная электронная конфигурация:
electron_conf = chemhelper.getElectronConfiguration(element)

# Электронная конфигурация с инертным газом:
nb_elecron_conf = chemhelper.getNobleGasElectronConfiguration(element)

print("Элемент {0} имеет молярную массу {1}, атомный номер {2},\nэлектронную конфигурацию {3}\nили с формой инертного газа {4}".format(name, molar_mass, atomic_number, electron_conf, nb_elecron_conf))


# Вычисление молярной массы молекулы:
compound = "C6H8O7" # Брутто-формула лимонной кислоты
glucose = chemhelper.Compound(compound)
text = glucose.getMolarMass()
print("Молярная масса " + compound + " = " + str(text))

