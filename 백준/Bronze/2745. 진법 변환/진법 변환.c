#include <stdio.h>
#include <string.h>

int main() {
  char N[10000];
  int B, l, t = 0, x = 1;

  scanf("%s %d", N, &B);
  l = strlen(N);

  for (int i = 0; i < l; i++) {
    if (N[l - i - 1] >= 48 && N[l - i - 1] <= 57) {
      t += (N[l - i - 1] - 48) * x;
    } else
      t += (N[l - i - 1] - 55) * x;
    x *= B;
  }
  printf("%d", t);
}