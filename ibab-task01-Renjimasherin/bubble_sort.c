#include<stdio.h>

void main()
{
int a[50],i,n,j,temp;  // Declaring array 'a' and variables i, n, j, temp
printf("\nBubble sort\n");
printf("\n--------------------------------\n");
printf("\nEnter the number of elements\n");
scanf("%d",&n); // Read number of elements from the user
printf("\nEnter the elements\n");

for (i=0;i<n;i++)
{
scanf("%d",&a[i]); // Stores each input value in a[i]
}
for (i=0;i<n-1;i++)
{
for (j=n-1;j>i;j--)
{
if(a[j]<a[j-1])  // Compares current element with the previous element
{
// Swap a[j] and a[j-1] if they are in wrong order
temp=a[j];
a[j]=a[j-1];
a[j-1]=temp;
}
}
}
printf("\n--------------------------------\n");
printf("\nSorted array is\n");
for (i=0;i<n;i++)
{
printf("%d\n",a[i]); // Prints each element on a new line
}
}

