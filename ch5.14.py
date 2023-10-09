def main():
    mass=float(input("Enter the object’s mass in kilograms:"))
    velocity=float(input("Enter the object’s velocity in meters per second:"))
    k_E=kinetic_energy(mass,velocity)
    print(f'kinetic energy={k_E:,.2f}')
def kinetic_energy(m,v):
    KE=1/2*m*v**2
    return KE
main()