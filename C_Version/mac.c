#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <iphlpapi.h>

#pragma comment(lib, "iphlpapi.lib")

int main()
{
    IP_ADAPTER_INFO *adapterInfo;
    IP_ADAPTER_INFO *adapter;

    DWORD bufferSize = 0;

    printf("========================================\n");
    printf("          MAC ADDRESS FINDER\n");
    printf("========================================\n\n");

    // Find the required buffer size
    GetAdaptersInfo(NULL, &bufferSize);

    // Allocate memory
    adapterInfo = (IP_ADAPTER_INFO *)malloc(bufferSize);

    if (adapterInfo == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Get network adapter information
    if (GetAdaptersInfo(adapterInfo, &bufferSize) == NO_ERROR)
    {
        adapter = adapterInfo;

        while (adapter != NULL)
        {
            printf("Interface  : %s\n", adapter->Description);

            printf("MAC Address: ");

            for (int i = 0; i < adapter->AddressLength; i++)
            {
                printf("%02X", adapter->Address[i]);

                if (i < adapter->AddressLength - 1)
                {
                    printf("-");
                }
            }

            printf("\n");
            printf("----------------------------------------\n");

            adapter = adapter->Next;
        }
    }
    else
    {
        printf("Unable to retrieve network adapter information.\n");
    }

    free(adapterInfo);

    printf("\n========================================\n");

    return 0;
}