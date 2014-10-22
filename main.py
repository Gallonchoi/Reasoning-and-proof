import logging


class Fact(object):
    """
    Fact
    """
    left_child = None
    right_child = None

    def __init__(self):
        # TODO:
        pass


class RulesForProposition(object):
    """
    Rules of inference for proposition
    """
    
    def __init__(self):
        pass

    def simplification(self):
        """
        (G && H) => G
        """
        pass

    def addition(self):
        """
        G => (G || H)
        """
        pass

    def disjunctive_syllogism(self):
        """
        !G, (G || H) => H
        """
        pass

    def modus_ponens(self):
        """
        G, (G -> H) => H
        """
        pass

    def modus_tollens(self):
        """
        !H, (G -> H) => !G
        """
        pass

    def hypothetical_syllogism(self):
        """
        (G -> H), (H -> I) => (G -> I)
        """
        pass

    def dilemma(self):
        """
        (G || H), (G -> I), (H -> I) => I
        """
        pass


class RulesForPredicate(object):
    pass


class Deduction(object):
    def RuleP(object):
        pass

    def RuleT(object):
        pass

    def RuleCP(object):
        pass


def main():
    logging.info('Running...')
    # TODO: input premises and conclusion

if __name__ == "__main__":
    main()
