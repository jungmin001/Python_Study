#include "Manager.h"

#include <iostream>
#include <vector>
#include <algorithm>

Game::Game()
{
    PlayerName = "Player";

    Level = 1;

    MaxHP = 100;
    HP = MaxHP;

    MaxMP = 30;
    MP = MaxMP;

    AttackPower = 15;
    Defense = 5;

    EXP = 0;
    NextEXP = 50;

    Gold = 30;
    Potion = 3;

    Floor = 1;

    IsRunning = true;

    EnemyHP = 0;
    EnemyMaxHP = 0;
    EnemyAttack = 0;

    EnemyGold = 0;
    EnemyEXP = 0;

    IsBoss = false;

    std::random_device Device;
    RandomEngine.seed(Device());
}

void Game::Start()
{
    ShowTitle();

    std::cout << "모험가의 이름을 입력하세요.\n";
    std::cout << "> ";

    std::getline(std::cin, PlayerName);

    if (PlayerName.empty())
    {
        PlayerName = "모험가";
    }

    std::cout << "\n";
    std::cout << PlayerName << "은(는) 오래된 던전 앞에 섰다.\n";
    std::cout << "던전 최심부에는 심연의 군주가 잠들어 있다고 한다.\n";

    MainLoop();
}

void Game::MainLoop()
{
    while (IsRunning)
    {
        if (HP <= 0)
        {
            GameOver();
            break;
        }

        if (Floor > 10)
        {
            Ending();
            break;
        }

        ShowMenu();

        int Choice = ReadChoice(1, 5);

        switch (Choice)
        {
        case 1:
            Explore();
            break;

        case 2:
            Shop();
            break;

        case 3:
            Inn();
            break;

        case 4:
            ShowStatus();
            break;

        case 5:
            IsRunning = false;
            std::cout << "\n게임을 종료합니다.\n";
            break;
        }
    }
}

void Game::ShowTitle()
{
    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "          ABYSS DUNGEON RPG\n";
    std::cout << "             심연의 던전\n";
    std::cout << "========================================\n";
}

void Game::ShowMenu()
{
    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "              던전 " << Floor << "층\n";
    std::cout << "========================================\n";

    std::cout << PlayerName << "  Lv." << Level << "\n";

    std::cout
        << "HP "
        << HP
        << "/"
        << MaxHP
        << "  ";

    std::cout
        << "MP "
        << MP
        << "/"
        << MaxMP
        << "\n";

    std::cout << "Gold : " << Gold << "\n";

    std::cout << "\n";
    std::cout << "[1] 던전 탐험\n";
    std::cout << "[2] 상점\n";
    std::cout << "[3] 여관\n";
    std::cout << "[4] 상태 확인\n";
    std::cout << "[5] 게임 종료\n";

    std::cout << "\n> ";
}

void Game::ShowStatus()
{
    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "             PLAYER STATUS\n";
    std::cout << "========================================\n";

    std::cout << "이름      : " << PlayerName << "\n";
    std::cout << "레벨      : " << Level << "\n";

    std::cout
        << "HP        : "
        << HP
        << "/"
        << MaxHP
        << "\n";

    std::cout
        << "MP        : "
        << MP
        << "/"
        << MaxMP
        << "\n";

    std::cout << "공격력    : " << AttackPower << "\n";
    std::cout << "방어력    : " << Defense << "\n";

    std::cout
        << "EXP       : "
        << EXP
        << "/"
        << NextEXP
        << "\n";

    std::cout << "Gold      : " << Gold << "\n";
    std::cout << "회복 물약 : " << Potion << "\n";
}

void Game::Explore()
{
    std::cout << "\n";
    std::cout << PlayerName << "은(는) 어두운 통로로 들어갔다.\n";

    if (Floor == 5 || Floor == 10)
    {
        CreateBoss();

        if (Battle())
        {
            Floor++;
        }

        return;
    }

    int Event = RandomRange(1, 100);

    if (Event <= 70)
    {
        CreateEnemy();

        if (Battle())
        {
            Floor++;
        }
    }
    else
    {
        RandomEvent();

        if (HP > 0)
        {
            Floor++;
        }
    }
}

void Game::CreateEnemy()
{
    std::vector<std::string> EnemyNames =
    {
        "굶주린 고블린",
        "동굴 늑대",
        "망령 병사",
        "부패한 기사",
        "심연의 주술사",
        "광기의 추적자"
    };

    int Index = RandomRange(
        0,
        static_cast<int>(EnemyNames.size()) - 1
    );

    EnemyName = EnemyNames[Index];

    EnemyMaxHP =
        35 +
        Floor * 12 +
        RandomRange(-5, 10);

    EnemyHP = EnemyMaxHP;

    EnemyAttack =
        7 +
        Floor * 2 +
        RandomRange(0, 3);

    EnemyGold =
        10 +
        Floor * 5 +
        RandomRange(0, 10);

    EnemyEXP =
        20 +
        Floor * 8;

    IsBoss = false;
}

void Game::CreateBoss()
{
    IsBoss = true;

    if (Floor == 5)
    {
        EnemyName = "철갑 오우거 그룸";

        EnemyMaxHP = 180;
        EnemyHP = EnemyMaxHP;

        EnemyAttack = 25;

        EnemyGold = 100;
        EnemyEXP = 150;
    }
    else
    {
        EnemyName = "심연의 군주 아자르";

        EnemyMaxHP = 350;
        EnemyHP = EnemyMaxHP;

        EnemyAttack = 38;

        EnemyGold = 300;
        EnemyEXP = 400;
    }
}

bool Game::Battle()
{
    std::cout << "\n";

    if (IsBoss)
    {
        std::cout << "========================================\n";
        std::cout << "              BOSS BATTLE\n";
        std::cout << "========================================\n";
    }

    std::cout << EnemyName << "이(가) 나타났다!\n";

    while (HP > 0 && EnemyHP > 0)
    {
        std::cout << "\n";

        std::cout << PlayerName << "\n";
        std::cout
            << CreateHPBar(HP, MaxHP)
            << " "
            << HP
            << "/"
            << MaxHP
            << "\n";

        std::cout << "\n";

        std::cout << EnemyName << "\n";
        std::cout
            << CreateHPBar(EnemyHP, EnemyMaxHP)
            << " "
            << EnemyHP
            << "/"
            << EnemyMaxHP
            << "\n";

        std::cout << "\n";
        std::cout << "[1] 공격\n";
        std::cout << "[2] 강공격     MP 8\n";
        std::cout << "[3] 회복 물약\n";
        std::cout << "[4] 도망\n";

        std::cout << "\n> ";

        int Choice = ReadChoice(1, 4);

        bool TurnUsed = true;

        switch (Choice)
        {
        case 1:
            PlayerAttack();
            break;

        case 2:
            if (!PlayerStrongAttack())
            {
                TurnUsed = false;
            }
            break;

        case 3:
            if (!UsePotion())
            {
                TurnUsed = false;
            }
            break;

        case 4:
        {
            if (IsBoss)
            {
                std::cout << "\n보스전에서는 도망칠 수 없다!\n";
                TurnUsed = false;
                break;
            }

            if (RandomRange(1, 100) <= 45)
            {
                std::cout << "\n전투에서 도망쳤다.\n";
                return false;
            }

            std::cout << "\n도망에 실패했다!\n";
            break;
        }
        }

        if (!TurnUsed)
        {
            continue;
        }

        if (EnemyHP <= 0)
        {
            break;
        }

        EnemyTurn();
    }

    if (HP <= 0)
    {
        return false;
    }

    VictoryReward();

    return true;
}

void Game::PlayerAttack()
{
    int Damage =
        AttackPower +
        RandomRange(-3, 5);

    if (Damage < 1)
    {
        Damage = 1;
    }

    bool Critical =
        RandomRange(1, 100) <= 15;

    if (Critical)
    {
        Damage *= 2;

        std::cout << "\n치명타!\n";
    }

    EnemyHP -= Damage;

    if (EnemyHP < 0)
    {
        EnemyHP = 0;
    }

    std::cout
        << EnemyName
        << "에게 "
        << Damage
        << "의 피해!\n";
}

bool Game::PlayerStrongAttack()
{
    const int ManaCost = 8;

    if (MP < ManaCost)
    {
        std::cout << "\nMP가 부족합니다.\n";
        return false;
    }

    MP -= ManaCost;

    int Damage =
        AttackPower * 2 +
        RandomRange(5, 12);

    EnemyHP -= Damage;

    if (EnemyHP < 0)
    {
        EnemyHP = 0;
    }

    std::cout << "\n강공격!\n";

    std::cout
        << EnemyName
        << "에게 "
        << Damage
        << "의 강력한 피해!\n";

    return true;
}

bool Game::UsePotion()
{
    if (Potion <= 0)
    {
        std::cout << "\n회복 물약이 없습니다.\n";
        return false;
    }

    if (HP >= MaxHP)
    {
        std::cout << "\n이미 HP가 가득 차 있습니다.\n";
        return false;
    }

    Potion--;

    int BeforeHP = HP;

    HP += 50;

    if (HP > MaxHP)
    {
        HP = MaxHP;
    }

    std::cout
        << "\n회복 물약 사용!\nHP "
        << HP - BeforeHP
        << " 회복!\n";

    return true;
}

void Game::EnemyTurn()
{
    int Damage =
        EnemyAttack +
        RandomRange(-2, 3);

    bool StrongAttack =
        RandomRange(1, 100) <= 20;

    if (StrongAttack)
    {
        Damage =
            static_cast<int>(
                Damage * 1.5
            );

        std::cout
            << "\n"
            << EnemyName
            << "의 강력한 공격!\n";
    }
    else
    {
        std::cout
            << "\n"
            << EnemyName
            << "의 공격!\n";
    }

    int ActualDamage =
        Damage - Defense;

    if (ActualDamage < 1)
    {
        ActualDamage = 1;
    }

    HP -= ActualDamage;

    if (HP < 0)
    {
        HP = 0;
    }

    std::cout
        << PlayerName
        << "은(는) "
        << ActualDamage
        << "의 피해를 입었다.\n";
}

void Game::RandomEvent()
{
    int Event =
        RandomRange(1, 4);

    std::cout << "\n";

    switch (Event)
    {
    case 1:
    {
        int Reward =
            RandomRange(20, 50);

        Gold += Reward;

        std::cout << "오래된 보물상자를 발견했다!\n";
        std::cout << Reward << " Gold 획득!\n";

        break;
    }

    case 2:
    {
        int Heal =
            RandomRange(20, 50);

        int BeforeHP = HP;

        HP += Heal;

        if (HP > MaxHP)
        {
            HP = MaxHP;
        }

        std::cout << "신비로운 샘물을 발견했다.\n";
        std::cout << "HP " << HP - BeforeHP << " 회복!\n";

        break;
    }

    case 3:
    {
        int Damage =
            RandomRange(10, 25);

        Damage -= Defense;

        if (Damage < 1)
        {
            Damage = 1;
        }

        HP -= Damage;

        if (HP < 0)
        {
            HP = 0;
        }

        std::cout << "숨겨진 함정을 밟았다!\n";
        std::cout << Damage << "의 피해를 입었다.\n";

        break;
    }

    case 4:
    {
        Potion++;

        std::cout << "버려진 가방을 발견했다.\n";
        std::cout << "회복 물약 +1\n";

        break;
    }
    }
}

void Game::Shop()
{
    while (true)
    {
        std::cout << "\n";
        std::cout << "========================================\n";
        std::cout << "                  SHOP\n";
        std::cout << "========================================\n";

        std::cout << "Gold : " << Gold << "\n\n";

        std::cout << "[1] 회복 물약      15 Gold\n";
        std::cout << "[2] 무기 강화      50 Gold\n";
        std::cout << "[3] 방어구 강화    50 Gold\n";
        std::cout << "[4] 나가기\n";

        std::cout << "\n> ";

        int Choice = ReadChoice(1, 4);

        switch (Choice)
        {
        case 1:
            if (Gold >= 15)
            {
                Gold -= 15;
                Potion++;

                std::cout << "\n회복 물약 +1\n";
            }
            else
            {
                std::cout << "\nGold가 부족합니다.\n";
            }

            break;

        case 2:
            if (Gold >= 50)
            {
                Gold -= 50;
                AttackPower += 3;

                std::cout << "\n무기를 강화했습니다.\n";
                std::cout << "공격력 +3\n";
            }
            else
            {
                std::cout << "\nGold가 부족합니다.\n";
            }

            break;

        case 3:
            if (Gold >= 50)
            {
                Gold -= 50;
                Defense += 2;

                std::cout << "\n방어구를 강화했습니다.\n";
                std::cout << "방어력 +2\n";
            }
            else
            {
                std::cout << "\nGold가 부족합니다.\n";
            }

            break;

        case 4:
            return;
        }
    }
}

void Game::Inn()
{
    const int Price = 15;

    std::cout << "\n";
    std::cout << "여관 주인 : \"15 Gold면 푹 쉬다 갈 수 있네.\"\n\n";

    std::cout << "[1] 숙박\n";
    std::cout << "[2] 나가기\n";

    std::cout << "\n> ";

    int Choice = ReadChoice(1, 2);

    if (Choice == 2)
    {
        return;
    }

    if (Gold < Price)
    {
        std::cout << "\nGold가 부족합니다.\n";
        return;
    }

    Gold -= Price;

    HP = MaxHP;
    MP = MaxMP;

    std::cout << "\n충분한 휴식을 취했다.\n";
    std::cout << "HP와 MP가 모두 회복되었다.\n";
}

void Game::VictoryReward()
{
    std::cout << "\n";
    std::cout << EnemyName << " 처치!\n";

    Gold += EnemyGold;
    EXP += EnemyEXP;

    std::cout << "Gold +" << EnemyGold << "\n";
    std::cout << "EXP +" << EnemyEXP << "\n";

    while (EXP >= NextEXP)
    {
        EXP -= NextEXP;

        LevelUp();
    }
}

void Game::LevelUp()
{
    Level++;

    NextEXP =
        static_cast<int>(
            NextEXP * 1.4
        );

    MaxHP += 20;
    MaxMP += 5;

    AttackPower += 4;
    Defense += 2;

    HP = MaxHP;
    MP = MaxMP;

    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "               LEVEL UP!\n";
    std::cout << "========================================\n";

    std::cout << "Lv." << Level << "\n";

    std::cout << "최대 HP +20\n";
    std::cout << "최대 MP +5\n";
    std::cout << "공격력 +4\n";
    std::cout << "방어력 +2\n";

    std::cout << "HP와 MP가 모두 회복되었습니다.\n";
}

void Game::GameOver()
{
    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "               GAME OVER\n";
    std::cout << "========================================\n";

    std::cout
        << PlayerName
        << "의 모험은 이곳에서 끝났다.\n";

    IsRunning = false;
}

void Game::Ending()
{
    std::cout << "\n";
    std::cout << "========================================\n";
    std::cout << "                 ENDING\n";
    std::cout << "========================================\n";

    std::cout << "\n";

    std::cout << "심연의 군주가 쓰러졌다.\n";
    std::cout << "던전을 뒤덮고 있던 어둠이 천천히 사라졌다.\n\n";

    std::cout
        << PlayerName
        << "은(는) 던전에서 살아 돌아왔다.\n\n";

    std::cout << "사람들은 새로운 영웅의 이름을 기억했다.\n";

    std::cout << "\n";
    std::cout << PlayerName << "\n";

    std::cout << "\n";
    std::cout << "                THE END\n";

    IsRunning = false;
}

int Game::RandomRange(int Min, int Max)
{
    std::uniform_int_distribution<int> Distribution(
        Min,
        Max
    );

    return Distribution(RandomEngine);
}

int Game::ReadChoice(int Min, int Max)
{
    while (true)
    {
        std::string Input;

        std::getline(
            std::cin,
            Input
        );

        try
        {
            int Value =
                std::stoi(Input);

            if (
                Value >= Min &&
                Value <= Max
            )
            {
                return Value;
            }
        }
        catch (...)
        {
        }

        std::cout << "올바른 번호를 입력하세요.\n> ";
    }
}

std::string Game::CreateHPBar(
    int Current,
    int Max
)
{
    const int Length = 20;

    double Ratio =
        static_cast<double>(Current)
        / Max;

    if (Max <= 0)
    {
        return std::string("[") + std::string(Length, '-') + "]";
    }

    int Filled =
        static_cast<int>(
            Ratio * Length
        );

    const auto Clamp = [](int Value, int Min, int MaxValue) -> int
    {
        return std::max(Min, std::min(Value, MaxValue));
    };

    Filled = Clamp(Filled, 0, Length);

    std::string Bar = "[";

    for (int i = 0; i < Length; i++)
    {
        if (i < Filled)
        {
            Bar += "#";
        }
        else
        {
            Bar += "-";
        }
    }

    Bar += "]";

    return Bar;
}

int main()
{
    Game game;

    game.Start();

    return 0;
}