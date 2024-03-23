import { signIn, signOut, useSession } from "next-auth/react";
import Head from "next/head";
import { useEffect, useState } from "react";

export default function Home() {
  const { data: session, status } = useSession();
  const [data, setData] = useState([]);


  useEffect(() => {
    if (session) {
      (async () => {
        const result = await fetch("http://127.0.0.1:8000/books/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${session.accessToken}`,
          },
        });
        console.log(result)
        const json = await result.json();
        setData(json);
      })();
    }
  }, [session]);

  return (
    <>
      <Head>
        <title>Django + NextAuth.js</title>
        <meta
          name="description"
          content="Django + NextAuth.js minimal example."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        {status === "loading" ? (
          ""
        ) : (
          <>
            {session ? (
              <>
                <h1>Hello, you've logged in!</h1>
                <p>{JSON.stringify(data)}</p>
                <a
                  href="/api/auth/signout"
                  onClick={(e) => {
                    e.preventDefault();
                    signOut();
                  }}
                >
                  Logout
                </a>
              </>
            ) : (
              <>
                <h1>Access Denied</h1>
                <p>
                  <a
                    href="/api/auth/signin"
                    onClick={(e) => {
                      e.preventDefault();
                      signIn();
                    }}
                  >
                    You must be signed in to view this page
                  </a>
                </p>
              </>
            )}
          </>
        )}
      </main>
    </>
  );
}
