// One canonical host: www.applesorchard.in -> applesorchard.in (301, keeps path and query).
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www.applesorchard.in") return Response.redirect("https://applesorchard.in" + url.pathname + url.search, 301);
  return context.next();
}
