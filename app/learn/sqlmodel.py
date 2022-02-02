"""
    1, when working with sqlmodel ,after creating the engine
      any request that we want to make to the database, we create a session

    2, the session is created as follows:
            session = Session(engine)

    3, then we do sesion.{command}()

    4, then we commit the session if data is added
            session.commit()
    5, then we close the connection
            session.close()

    Extra we can use The "with" to create session as
        with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()

"""