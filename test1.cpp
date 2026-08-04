
#include "test1.h"

using namespace std;

void BeginPlay()
{
    /* Tick StartSetting*/
    bIsCanTick = true;


    bIsAlive = true;
    MaxHealth = 100.f;
    CurrentHealth = MaxHealth;

    DefaultMainUI();
    InputF();
    cout << "You re Input Key :" << InputKey << endl;
}

void TickFunction(int TickTimer)
{
    while(true) 
    {
        if (TickTimer % 2 != 0)
        {
            Tick();
        }
    }
}

void Tick(int DeltaTime)
{
    TickFunction(DeltaTime);
}

void OnTakeDamage(float Damage)
{
    CurrentHealth += Damage;

    if(CurrentHealth <= 0) Die();
}

void Die()
{
    cout << "Player Die!" << endl;
}

float GetHealth()
{
    return CurrentHealth;
}

void SetHealth(float Value)
{
    CurrentHealth += Value;
}

void DefaultMainUI()
{
    cout << "======================================================" << endl;
    cout << "==                     HELLO                        ==" << endl;
    cout << "======================================================" << endl;

}

int InputF()
{
    
    cout << "===| 번호를 입력 하세요 |===";
    cin >> InputKey;
    return InputKey;
}

int main()
{
    BeginPlay();
    if (bIsCanTick) TickFunction(1);
    return 0;
}