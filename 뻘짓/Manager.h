#pragma once

#include <string>
#include <random>

using namespace std;

class Game
{
private:
    // 플레이어
    std::string PlayerName;

    int Level;
    int HP;
    int MaxHP;
    int MP;
    int MaxMP;

    int AttackPower;
    int Defense;

    int EXP;
    int NextEXP;

    int Gold;
    int Potion;

    // 게임 진행
    int Floor;
    bool IsRunning;

    // 몬스터
    std::string EnemyName;

    int EnemyHP;
    int EnemyMaxHP;
    int EnemyAttack;

    int EnemyGold;
    int EnemyEXP;

    bool IsBoss;

    // 랜덤
    std::mt19937 RandomEngine;

public:
    Game();

    void Start();

private:
    void MainLoop();

    void ShowTitle();
    void ShowMenu();
    void ShowStatus();

    void Explore();

    void CreateEnemy();
    void CreateBoss();

    bool Battle();

    void PlayerAttack();
    bool PlayerStrongAttack();
    bool UsePotion();

    void EnemyTurn();

    void RandomEvent();

    void Shop();
    void Inn();

    void VictoryReward();
    void LevelUp();

    void GameOver();
    void Ending();

    int RandomRange(int Min, int Max);
    int ReadChoice(int Min, int Max);

    std::string CreateHPBar(int Current, int Max);
};