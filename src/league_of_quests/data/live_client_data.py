from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class Ability(BaseModel):
    abilityLevel: Optional[int] = None
    displayName: str
    id: str
    rawDescription: str
    rawDisplayName: str


class Abilities(BaseModel):
    E: Optional[Ability] = None
    Passive: Optional[Ability] = None
    Q: Optional[Ability] = None
    R: Optional[Ability] = None
    W: Optional[Ability] = None


class ChampionStats(BaseModel):
    abilityHaste: float
    abilityPower: float
    armor: float
    armorPenetrationFlat: float
    armorPenetrationPercent: float
    attackDamage: float
    attackRange: float
    attackSpeed: float
    bonusArmorPenetrationPercent: float
    bonusMagicPenetrationPercent: float
    critChance: float
    critDamage: float
    currentHealth: float
    healShieldPower: float
    healthRegenRate: float
    lifeSteal: float
    magicLethality: float
    magicPenetrationFlat: float
    magicPenetrationPercent: float
    magicResist: float
    maxHealth: float
    moveSpeed: float
    omnivamp: float
    physicalLethality: float
    physicalVamp: float
    resourceMax: Optional[float] = None
    resourceRegenRate: Optional[float] = None
    resourceType: Optional[str] = None
    resourceValue: Optional[float] = None
    spellVamp: float
    tenacity: float


class Rune(BaseModel):
    displayName: str
    id: int
    rawDescription: str
    rawDisplayName: str


class StatRune(BaseModel):
    id: int
    rawDescription: str


class FullRunes(BaseModel):
    generalRunes: List[Rune]
    keystone: Rune
    primaryRuneTree: Rune
    secondaryRuneTree: Rune
    statRunes: List[StatRune]


class ActivePlayer(BaseModel):
    abilities: Abilities
    championStats: ChampionStats
    currentGold: float
    fullRunes: FullRunes
    level: int
    riotId: str
    riotIdGameName: str
    riotIdTagLine: str
    summonerName: str
    teamRelativeColors: bool


class Item(BaseModel):
    canUse: bool
    consumable: bool
    count: int
    displayName: str
    itemID: int
    price: int
    rawDescription: str
    rawDisplayName: str
    slot: int


class PlayerRunes(BaseModel):
    keystone: Rune
    primaryRuneTree: Rune
    secondaryRuneTree: Rune


class Scores(BaseModel):
    assists: int
    creepScore: int
    deaths: int
    kills: int
    wardScore: float


class SummonerSpell(BaseModel):
    displayName: str
    rawDescription: str
    rawDisplayName: str


class SummonerSpells(BaseModel):
    summonerSpellOne: SummonerSpell
    summonerSpellTwo: SummonerSpell


class Player(BaseModel):
    championName: str
    isBot: bool
    isDead: bool
    items: List[Item]
    level: int
    position: str
    rawChampionName: str
    rawSkinName: str
    respawnTimer: float
    riotId: str
    riotIdGameName: str
    riotIdTagLine: str
    runes: PlayerRunes
    scores: Scores
    skinID: int
    skinName: str
    summonerName: str
    summonerSpells: SummonerSpells
    team: str


class Event(BaseModel):
    EventID: int
    EventName: str
    EventTime: float
    Assisters: Optional[List[str]] = None
    KillerName: Optional[str] = None
    VictimName: Optional[str] = None
    Recipient: Optional[str] = None
    TurretKilled: Optional[str] = None
    DragonType: Optional[str] = None
    Stolen: Optional[str] = None
    InhibKilled: Optional[str] = None
    Acer: Optional[str] = None
    AcingTeam: Optional[str] = None
    InhibRespawned: Optional[str] = None
    Result: Optional[str] = None


class Events(BaseModel):
    Events: List[Event]


class GameData(BaseModel):
    gameMode: str
    gameTime: float
    mapName: str
    mapNumber: int
    mapTerrain: str


class LiveClientData(BaseModel):
    activePlayer: ActivePlayer
    allPlayers: List[Player]
    events: Events
    gameData: GameData
