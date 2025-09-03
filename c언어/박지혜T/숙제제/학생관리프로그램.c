#include <stdio.h>
int main() {
    struct Student{
        char name[50];
        int math;
        int english;
        int science;
    };
    struct Student students[100];
    int count=0;
    int choice;
    char searchName[50];
    while(1){
        printf("\n1. 학생 추가\n2. 학생 성적 조회\n3. 학생 성적 수정\n4. 종료\n선택: ");
        scanf("%d", &choice);
        if(choice==1){
            if(count>=100){
                printf("학생 수 초과\n");
                continue;
            }
            printf("이름: ");
            scanf("%s", students[count].name);
            printf("수학 점수: ");
            scanf("%d", &students[count].math);
            printf("영어 점수: ");
            scanf("%d", &students[count].english);
            printf("과학 점수: ");
            scanf("%d", &students[count].science);
            count++;
        } else if(choice==2) {
            printf("조회할 학생 이름: ");
            scanf("%s", searchName);
            int found=0;
            for(int i=0;i<count;i++){
                int same=1;
                int j=0;
                while(searchName[j]!='\0' || students[i].name[j]!='\0'){
                    if(searchName[j]!=students[i].name[j]) {
                        same=0;
                        break;
                    }
                    j++;
                }
                if(same){
                    printf("%s - 수학: %d, 영어: %d, 과학: %d\n",
                           students[i].name,
                           students[i].math,
                           students[i].english,
                           students[i].science);
                    found = 1;
                    break;
                }
            }
            if(!found) {
                printf("학생을 찾을 수 없습니다.\n");
            }
        } else if(choice==3) {
            printf("수정할 학생 이름: ");
            scanf("%s",searchName);
            int found=0;
            for(int i=0;i<count;i++){
                int same=1;
                int j=0;
                while(searchName[j]!='\0' || students[i].name[j]!='\0'){
                    if(searchName[j]!=students[i].name[j]){
                        same=0;
                        break;
                    }
                    j++;
                }
                if(same){
                    printf("새 수학 점수: ");
                    scanf("%d", &students[i].math);
                    printf("새 영어 점수: ");
                    scanf("%d", &students[i].english);
                    printf("새 과학 점수: ");
                    scanf("%d", &students[i].science);
                    printf("수정 완료\n");
                    found = 1;
                    break;
                }
            }
            if(!found) {
                printf("학생을 찾을 수 없습니다.\n");
            }
        } else if(choice==4){
            break;
        } else{
            printf("잘못된 선택입니다.\n");
        }
    }
    return 0;
}
