import psutil
import socket


def get_network_info():
    interfaces = psutil.net_if_addrs()
    interface_status = psutil.net_if_stats()

    network_data = []

    for interface, addresses in interfaces.items():

        mac_address = "Not Available"
        ipv4_address = "Not Available"

        for address in addresses:

            if address.family == psutil.AF_LINK:
                mac_address = address.address

            elif address.family == socket.AF_INET:
                ipv4_address = address.address

        # Find whether the interface is active or inactive
        status = "Inactive"

        if interface in interface_status:
            if interface_status[interface].isup:
                status = "Active"

        # Identify the type of network interface
        if "Wi-Fi" in interface:
            interface_type = "Wireless"

        elif "Ethernet" in interface:
            interface_type = "Wired"

        elif "Bluetooth" in interface:
            interface_type = "Bluetooth"

        elif "Loopback" in interface:
            interface_type = "Loopback"

        else:
            interface_type = "Other"

        network_data.append({
            "interface": interface,
            "type": interface_type,
            "mac": mac_address,
            "ip": ipv4_address,
            "status": status
        })

    return network_data


if __name__ == "__main__":

    network_data = get_network_info()

    for network in network_data:
        print("\nInterface:", network["interface"])
        print("Type:", network["type"])
        print("Status:", network["status"])
        print("MAC Address:", network["mac"])
        print("IPv4 Address:", network["ip"])