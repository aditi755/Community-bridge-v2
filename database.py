from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://koehtbbjzuqq79ww33nf:pscale_pw_FCOblS4h6ksOUcsUhbxbLIkYlRiwjmWibma5aSlsDXi@ap-south.connect.psdb.cloud/communitybridge?"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.oem"
    }
  }
)

def load_communities_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM communities"))
        communities = []
        for row in result:
            community = {}
            keys = list(result.keys())
            for i in range(len(keys)):
                community[keys[i]] = row[i]
            communities.append(community)
        return communities





      








