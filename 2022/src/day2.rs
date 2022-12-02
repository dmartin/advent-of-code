use aoc_runner_derive::aoc;

enum HandType {
    Rock,
    Paper,
    Scissors,
}

impl From<&str> for HandType {
    fn from(s: &str) -> Self {
        match s {
            "A" | "X" => Self::Rock,
            "B" | "Y" => Self::Paper,
            "C" | "Z" => Self::Scissors,
            _ => panic!("invalid input"),
        }
    }
}

fn score_round(opponent_move: &HandType, your_move: &HandType) -> i32 {
    use HandType::*;

    let mut score = match your_move {
        Rock => 1,
        Paper => 2,
        Scissors => 3,
    };
    score += match (opponent_move, your_move) {
        (Rock, Rock) => 3,
        (Rock, Paper) => 6,
        (Rock, Scissors) => 0,
        (Paper, Rock) => 0,
        (Paper, Paper) => 3,
        (Paper, Scissors) => 6,
        (Scissors, Rock) => 6,
        (Scissors, Paper) => 0,
        (Scissors, Scissors) => 3,
    };
    score
}

mod part1 {
    use super::*;

    fn parse_strategy(input: &str) -> impl Iterator<Item = (HandType, HandType)> + '_ {
        input.lines().map(|round| {
            let round = round.split_once(' ').unwrap();
            (round.0.into(), round.1.into())
        })
    }

    #[aoc(day2, part1)]
    fn part1(input: &str) -> i32 {
        let strategy = parse_strategy(input);
        strategy.fold(0, |mut acc, round| {
            acc += score_round(&round.0, &round.1);
            acc
        })
    }
}

mod part2 {
    use super::*;

    enum OutcomeType {
        Win,
        Lose,
        Draw,
    }

    impl From<&str> for OutcomeType {
        fn from(s: &str) -> Self {
            match s {
                "X" => Self::Lose,
                "Y" => Self::Draw,
                "Z" => Self::Win,
                _ => panic!("invalid input"),
            }
        }
    }

    fn parse_strategy(input: &str) -> impl Iterator<Item = (HandType, OutcomeType)> + '_ {
        input.lines().map(|round| {
            let round = round.split_once(' ').unwrap();
            (round.0.into(), round.1.into())
        })
    }

    fn ensure_outcome(opponent_move: &HandType, outcome: &OutcomeType) -> HandType {
        use HandType::*;
        use OutcomeType::*;

        match (opponent_move, outcome) {
            (Rock, Win) => Paper,
            (Rock, Lose) => Scissors,
            (Rock, Draw) => Rock,
            (Paper, Win) => Scissors,
            (Paper, Lose) => Rock,
            (Paper, Draw) => Paper,
            (Scissors, Win) => Rock,
            (Scissors, Lose) => Paper,
            (Scissors, Draw) => Scissors,
        }
    }

    #[aoc(day2, part2)]
    fn part2(input: &str) -> i32 {
        let strategy = parse_strategy(input);
        strategy.fold(0, |mut acc, round| {
            acc += score_round(&round.0, &ensure_outcome(&round.0, &round.1));
            acc
        })
    }
}
