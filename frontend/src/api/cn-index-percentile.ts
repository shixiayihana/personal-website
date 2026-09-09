const API_PREFIX = '/api'

export type Valuation = {
  index_code: string
  index_name: string
  data: string
  pe_percentile: number
  pb_percentile: number
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_PREFIX}${path}`, init)

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`)
  }

  return response.json() as Promise<T>
}

export function getLatestValuations(): Promise<Valuation[]> {
  return request<Valuation[]>('/valuations/latest')
}