#include <stdio.h>
main() {
    char *amigos[] = {"juan", "liliana", "pablo", "maria", NULL};
    int i = 0;
    while(amigos[i] != NULL) { 
        char *nombre = amigos[i];
        printf("Nº %i - %s\n", i, nombre);
        i++;
    };
    return 0;
}
