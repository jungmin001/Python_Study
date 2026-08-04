#pragma once

#include "iostream"
#include "vector"
#include "map"

class FORCEINLINE;

using namespace std;

/* Default Function*/
void BeginPlay();
void Tick(int DeltaTime = 1);
void TickFunction(int TickTimer = 1);
int main();

float GetHealth();
void SetHealth(float Value);

void OnTakeDamage(float Damage);
void Die();

bool bIsCanTick;
bool bIsAlive;

float MaxHealth;
float CurrentHealth;

void DefaultMainUI();

/* Input */
int InputKey;
int InputF();

/// @brief 
/// @return 
//FORCEINLINE float GetterHealth() {return CurrentHealth};
//FORCEINLINE void SetterHealth() {};